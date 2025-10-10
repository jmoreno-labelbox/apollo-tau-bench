from domains.dto import Task, Action

TASKS = [
    # 1 - EXPERT COMPLEXITY (16 edges) DETERMINISTIC SKILL DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U001",
        instruction="As part of the 'Succession Planning' for the 'UX Design Lead' role, HR Partner Harper Bennett is actioning the development plan for candidate David Adams. First, find the relevant workflow and update the 'Development Planning' stage to 'In Progress'. Next, find his skill gap analysis for the 'DesignOps Lead' role. Based on the recommended course for his 'Stakeholder Alignment' gap, enroll him in the training. Then, find an available mentor with 'Leadership' expertise and link them. Finally, set a new active goal with ID 'G304-2', type 'Leadership', description 'Complete PMP course and lead stakeholder alignment for one cross-functional project.', with a last updated date of '2025-09-10'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "David Adams"},
            ),
            Action(
                name="find_workflow",
                kwargs={"employee_id": "U304", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Development Planning",
                    "status": "In Progress",
                },
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-2",
                        "goal_type": "Leadership",
                        "goal_description": "Complete PMP course and lead stakeholder alignment for one cross-functional project.",
                        "status": "Active",
                        "last_updated": "2025-09-10",
                    },
                },
            ),
        ],
        outputs=[
            '{"success": "Development Planning -> In Progress"}',
            '{"success": "U304 enrolled in C1004"}',
            '{"success": "Mentor M100 -> U304"}',
            '{"success": "Goal set for U304"}',
        ],
    ),
    # 2 - HIGH COMPLEXITY
    Task(
        annotator="synth",
        user_id="U308",
        instruction="U308 should develop Project Management skills for UX Writer role advancement. Analyze skill gaps, search for relevant courses, and enroll in C1004 (Project Management).",
        actions=[
            Action(name="get_user_profile", kwargs={"user_id": "U308"}),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(name="get_user_certification", kwargs={"user_id": "U308"}),
            Action(name="get_user_course_progress", kwargs={"user_id": "U308"}),
            Action(
                name="get_performance_review",
                kwargs={"user_id": "U308", "period": "Q3 2024"},
            ),
            Action(name="get_team_training_log", kwargs={"team_id": "T006"}),
            Action(name="search_courses", kwargs={"skill": "Project Management"}),
            Action(name="get_user_certification", kwargs={"user_id": "U308"}),
            Action(name="get_user_course_progress", kwargs={"user_id": "U308"}),
            Action(
                name="get_performance_review",
                kwargs={"user_id": "U308", "period": "Q3 2024"},
            ),
            Action(name="get_team_training_log", kwargs={"team_id": "T006"}),
            Action(name="get_user_profile", kwargs={"user_id": "U308"}),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(name="get_user_certification", kwargs={"user_id": "U308"}),
            Action(name="get_user_course_progress", kwargs={"user_id": "U308"}),
            Action(
                name="assign_course", kwargs={"user_id": "U308", "course_id": "C1004"}
            ),
        ],
        outputs=["U308 enrolled in C1004"],
    ),
    # 3 - EXPERT COMPLEXITY (15 edges)- COMPREHENSIVE LEADERSHIP DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U003",
        instruction="As part of the 'DevOps Automation' project, team lead Mason Desai is creating a development plan for Alexander Adams. First, find Alexander and check his existing certifications. Then, get his skill gaps for the 'Staff SRE' role. Since no course is available for his 'Terraform' gap, find an available mentor with 'Engineering' expertise and link them. Next, update his 'Terraform' skill proficiency to 'Beginner'. Finally, set a new active goal with ID 'G306-3', type 'Skill Mastery', description 'Achieve Intermediate Terraform proficiency for DevOps Automation project.', with a last updated date of '2025-09-12', and log this action to the Engineering Team's training log with the following entry: 'Alexander Adams assigned mentor for Terraform skill development for DevOps Automation project.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="get_user_certification",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Engineering"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U306", "mentor_id": "M101"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U306",
                    "skill": "Terraform",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U306",
                    "goal": {
                        "goal_id": "G306-3",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Achieve Intermediate Terraform proficiency for DevOps Automation project.",
                        "status": "Active",
                        "last_updated": "2025-09-12",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T003",
                    "entry": "Alexander Adams assigned mentor for Terraform skill development for DevOps Automation project.",
                },
            ),
        ],
        outputs=[
            '{"success": "Mentor M101 -> U306"}',
            '{"success": "U306 Terraform -> Beginner"}',
            '{"success": "Goal set for U306"}',
            '{"success": "Log entry added for T003"}',
        ],
    ),
    # 4 - EXPERT COMPLEXITY (16 edges) CLOUD SECURITY SPECIALIZATION
    Task(
        annotator="synth",
        user_id="U004",
        instruction="To support his goal of earning the 'AWS Security Specialty' certification, Logan Garcia needs a foundational development plan. First, check his existing certifications. Then, find the job posting for 'Cloud Security Compliance Specialist' to identify a key foundational skill. Based on the 'Policy Writing' requirement, search for and assign the relevant course. Next, update his 'Policy Writing' skill proficiency to 'Intermediate'. Then, find an available mentor with 'Policy' expertise and link them. Finally, set a new active goal with ID 'G303-2', type 'Certification', description 'Complete foundational Policy Writing course for AWS Security certification path.', with a last updated date of '2025-08-20'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Logan Garcia"},
            ),
            Action(
                name="get_user_certification",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Cloud Security Compliance Specialist"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "Policy Writing"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U303", "course_id": "C1007"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U303",
                    "skill": "Policy Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Policy"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U303", "mentor_id": "M100"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Certification",
                        "goal_description": "Complete foundational Policy Writing course for AWS Security certification path.",
                        "status": "Active",
                        "last_updated": "2025-08-20",
                    },
                },
            ),
        ],
        outputs=[
            '{"success": "U303 enrolled in C1007"}',
            '{"success": "U303 Policy Writing -> Intermediate"}',
            '{"success": "Mentor M100 -> U303"}',
            '{"success": "Goal set for U303"}',
        ],
    ),
    # 5 - HIGH COMPLEXITY (13 edges) - SENIOR DATA SCIENTIST PREPARATION
    Task(
        annotator="synth",
        user_id="U005",
        instruction="To support Harper Bennett's transition to 'People Analytics Lead', please create a formal development plan. First, find her skill gap analysis for this role. Based on the identified gaps, assign her the courses for 'Statistical Modeling' and 'Data Visualization'. Next, find an available mentor with 'Leadership' expertise and link them to her. Finally, set a new active goal with ID 'G310-3', type 'Role Transition', description 'Complete statistical modeling and data visualization courses to lead the new People Analytics function.', with a last updated date of '2025-09-20'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1003"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U310",
                    "goal": {
                        "goal_id": "G310-3",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete statistical modeling and data visualization courses to lead the new People Analytics function.",
                        "status": "Active",
                        "last_updated": "2025-09-20",
                    },
                },
            ),
        ],
        outputs=[
            '{"success": "U310 enrolled in C1005"}',
            '{"success": "U310 enrolled in C1003"}',
            '{"success": "Mentor M102 -> U310"}',
            '{"success": "Goal set for U310"}',
        ],
    ),
    # 6 - HIGH COMPLEXITY (8 edges) - DEVOPS LEADERSHIP DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U006",
        instruction="As the Marketing Team lead preparing for the 'Product Marketing Launch' project, Harper King needs to formalize her development in data analytics, a key area from her performance review. First, retrieve the review. Then, find her skill gap analysis for the 'Product Marketing Specialist' role. Based on the 'Data Analytics' gap, assign her the recommended course. Next, find an available mentor with 'Career Growth' expertise and link them to her. Finally, update the 'Development Plan' stage in her performance review workflow to 'Completed' and add an entry to the Marketing Team's training log: 'Harper King assigned Data Analytics course for Product Marketing Launch project.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper King"},
            ),
            Action(
                name="get_performance_review",
                kwargs={"user_id": "U305", "period": "Q3 2024"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U305", "mentor_id": "M101"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T004",
                    "entry": "Harper King assigned Data Analytics course for Product Marketing Launch project.",
                },
            ),
        ],
        outputs=[
            '{"success": "U305 enrolled in C1003"}',
            '{"success": "Mentor M101 -> U305"}',
            '{"success": "Development Plan -> Completed"}',
            '{"success": "Log entry added for T004"}',
        ],
    ),
    # 7 - EXPERT COMPLEXITY (14 edges) - UX DESIGN LEADERSHIP TRANSITION
    Task(
        annotator="synth",
        user_id="U007",
        instruction="A manager is creating a development plan for Mason Desai's transition to 'Backend Tech Lead'. First, analyze his skill gaps for the role. Based on the 'Team Leadership' gap, assign him the correct course. Then, find an available mentor with 'Engineering' and 'Career Growth' expertise and link them. Next, update his 'Team Leadership' skill proficiency to 'Beginner'. Finally, set a new active goal with ID 'G312-3', type 'Role Transition', description 'Complete leadership training and lead one backend redesign initiative.', with a last updated date of '2025-09-25', and log this action to his team's training log with the following entry: 'Mason Desai assigned leadership training and mentor for Backend Tech Lead path.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Mason Desai"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U312", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U312", "mentor_id": "M101"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U312",
                    "skill": "Team Leadership",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U312",
                    "goal": {
                        "goal_id": "G312-3",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete leadership training and lead one backend redesign initiative.",
                        "status": "Active",
                        "last_updated": "2025-09-25",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U312"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T003",
                    "entry": "Mason Desai assigned leadership training and mentor for Backend Tech Lead path.",
                },
            ),
        ],
        outputs=[
            '{"success": "U312 enrolled in C1004"}',
            '{"success": "Mentor M101 -> U312"}',
            '{"success": "U312 Team Leadership -> Beginner"}',
            '{"success": "Goal set for U312"}',
            '{"success": "Log entry added for T003"}',
        ],
    ),
    # 8 - REPLACED
    Task(
        annotator="synth",
        user_id="U008",
        instruction="Hiring manager Jack Wang is reviewing Ava Nguyen's application for the 'Senior Data Scientist' role and has decided to put her on a development track. First, find her application and update its status to 'Rejected - Future Consideration'. Next, locate her 'Internal Promotion Process' workflow. In that workflow, update the 'Skills Assessment' stage to 'Completed' and the 'Development Plan' stage to 'In Progress'. Concurrently, check her skill gap for the 'Clinical Analytics Lead' role. Based on the identified 'Python' gap, assign her the correct course. Finally, find an available mentor with 'Leadership' expertise and link them to her.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP001",
                    "status": "Rejected - Future Consideration",
                },
            ),
            Action(
                name="find_workflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Internal Promotion Process",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Skills Assessment",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
        ],
        outputs=[],
    ),
    # 9 - HIGH COMPLEXITY (13 edges) - BACKEND LEADERSHIP DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U009",
        instruction="HR Partner Harper Bennett is actioning the 'Succession Planning' workflow for candidate David Adams. First, find the workflow and update the 'Development Planning' stage to 'In Progress'. Next, find his skill gap analysis for the 'DesignOps Lead' role. Based on his 'Stakeholder Alignment' gap, assign him the correct leadership course. Then, find an available mentor with 'Leadership' expertise and link them. Finally, set a new active goal with ID 'G304-3', type 'Leadership', description 'Complete leadership course and formalize one cross-team process.', with a last updated date of '2025-09-30', and log this action to his team's training log with the following entry: 'David Adams assigned leadership course and mentor as part of succession plan.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "David Adams"},
            ),
            Action(
                name="find_workflow",
                kwargs={"employee_id": "U304", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Development Planning",
                    "status": "In Progress",
                },
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-3",
                        "goal_type": "Leadership",
                        "goal_description": "Complete leadership course and formalize one cross-team process.",
                        "status": "Active",
                        "last_updated": "2025-09-30",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T002",
                    "entry": "David Adams assigned leadership course and mentor as part of succession plan.",
                },
            ),
        ],
        outputs=[
            '{"success": "Development Planning -> In Progress"}',
            '{"success": "U304 enrolled in C1004"}',
            '{"success": "Mentor M102 -> U304"}',
            '{"success": "Goal set for U304"}',
            '{"success": "Log entry added for T002"}',
        ],
    ),
    # 10 - REPLACED
    Task(
        annotator="synth",
        user_id="U010",
        instruction="As team lead for the Data Analytics Team, Jack Wang needs to prepare Ava Nguyen for the upcoming 'Predictive Modeling Initiative'. First, find Jack's team ID. Then, find Ava Nguyen and check her skill gap for the 'Clinical Analytics Lead' role. Based on the identified 'Python' gap, assign her the required course. After assigning, verify her enrollment status for that course. Next, add an entry to the team's training log: 'Ava Nguyen assigned Python training for Predictive Modeling project.' Finally, to formally track her development, update her proficiency for the 'Python' skill to 'Beginner'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Jack Wang"},
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U301"},
            ),
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="get_course_progress",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen assigned Python training for Predictive Modeling project.",
                },
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={"user_id": "U302", "skill": "Python", "new_level": "Beginner"},
            ),
        ],
        outputs=[],
    ),
    # 11 - HIGH COMPLEXITY (14 edges) - CLINICAL ANALYTICS PROGRESSION
    Task(
        annotator="synth",
        user_id="U011",
        instruction="For the upcoming 'Predictive Modeling Initiative', team lead Jack Wang needs to upskill Ava Nguyen. First, find Ava's application for the 'Senior Data Scientist' role to identify her key skill gap. Based on the 'Machine Learning' gap, assign her the correct course. Then, check her progress on this new course. Next, find an available mentor with 'Leadership' expertise and link them to her. Finally, update her 'Machine Learning' skill proficiency to 'Beginner' and add an entry to the Data Analytics Team's training log: 'Ava Nguyen assigned ML training for Predictive Modeling Initiative.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="get_job_application",
                kwargs={"application_id": "APP001"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="get_course_progress",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U302",
                    "skill": "Machine Learning",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen assigned ML training for Predictive Modeling Initiative.",
                },
            ),
        ],
        outputs=[
            '{"success": "U302 enrolled in C1005"}',
            '{"success": "Mentor M102 -> U302"}',
            '{"success": "U302 Machine Learning -> Beginner"}',
            '{"success": "Log entry added for T001"}',
        ],
    ),
    # 12 - REPLACED
    Task(
        annotator="synth",
        user_id="U012",
        instruction="Manager David Adams is preparing Chloe Scott for the 'UX Design Lead' role as part of the 'Succession Planning' workflow. First, find Chloe Scott's user ID. Then, locate the relevant workflow and update the 'Candidate Identification' stage to 'Completed' and the 'Skills Assessment' stage to 'In Progress'. Next, find her application for the 'UX Design Lead' job to identify her skill gaps. Based on her primary gap, 'Design Operations', search for relevant courses. Since no course is found, proceed to find an available mentor with 'Design' expertise and link them to Chloe. Finally, set a new active performance goal for her: goal_id 'G307-2', type 'Leadership', description 'Shadow a Design Lead on one project and present findings.', with a last updated date of '2025-07-10'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Chloe Scott"},
            ),
            Action(
                name="find_workflow",
                kwargs={"employee_id": "U307", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Candidate Identification",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Skills Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "UX Design Lead"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U307", "job_id": "J002"},
            ),
            Action(
                name="get_job_application",
                kwargs={"application_id": "APP005"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "Design Operations"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U307", "mentor_id": "M100"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U307",
                    "goal": {
                        "goal_id": "G307-2",
                        "goal_type": "Leadership",
                        "goal_description": "Shadow a Design Lead on one project and present findings.",
                        "status": "Active",
                        "last_updated": "2025-07-10",
                    },
                },
            ),
        ],
        outputs=[],
    ),
    # 13 - HIGH COMPLEXITY (13 edges) - CLINICAL ANALYTICS UPSKILLING
    Task(
        annotator="synth",
        user_id="U302",
        instruction="To support Harper Bennett's career goal of becoming a 'People Analytics Lead', please create a formal development plan. First, find her skill gap analysis for this target role. Based on the recommendations, assign her the courses for 'Statistical Modeling' and 'Data Visualization'. Next, find an available mentor with 'Leadership' expertise and link them to her. Finally, set a new active goal with ID 'G310-3', type 'Role Transition', description 'Complete statistical modeling and data visualization courses to lead the new People Analytics function.', with a last updated date of '2025-09-20'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1003"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U310",
                    "goal": {
                        "goal_id": "G310-3",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete statistical modeling and data visualization courses to lead the new People Analytics function.",
                        "status": "Active",
                        "last_updated": "2025-09-20",
                    },
                },
            ),
        ],
        outputs=[
            '{"success": "U310 enrolled in C1005"}',
            '{"success": "U310 enrolled in C1003"}',
            '{"success": "Mentor M102 -> U310"}',
            '{"success": "Goal set for U310"}',
        ],
    ),
    # 14 - EXPERT COMPLEXITY (16 edges) - ANALYTICS VISUALIZATION DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U014",
        instruction="For the new 'AR-based onboarding module' project, L&D lead Owen Walker needs to upskill team member Lucas Young in analytics. First, find Lucas and check his existing certifications. Then, search for a 'Tableau' course and assign it to him. Next, update his 'Tableau' skill proficiency to 'Beginner'. Then, find an available mentor with 'Career Growth' expertise and link them. Finally, set a new active goal with ID 'G311-2', type 'Skill Mastery', description 'Apply data visualization skills to measure the effectiveness of the new AR onboarding module.', with a last updated date of '2025-10-01', and log this action to the L&D team's training log with the following entry: 'Lucas Young assigned data visualization training for AR/VR project analytics.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Lucas Young"},
            ),
            Action(
                name="get_user_certification",
                kwargs={"user_id": "U311"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "Tableau"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U311", "course_id": "C1003"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U311",
                    "skill": "Tableau",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U311", "mentor_id": "M101"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U311",
                    "goal": {
                        "goal_id": "G311-2",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Apply data visualization skills to measure the effectiveness of the new AR onboarding module.",
                        "status": "Active",
                        "last_updated": "2025-10-01",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U311"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T007",
                    "entry": "Lucas Young assigned data visualization training for AR/VR project analytics.",
                },
            ),
        ],
        outputs=[
            '{"success": "U311 enrolled in C1003"}',
            '{"success": "U311 Tableau -> Beginner"}',
            '{"success": "Mentor M101 -> U311"}',
            '{"success": "Goal set for U311"}',
            '{"success": "Log entry added for T007"}',
        ],
    ),
    # 15 - REPLACED
    Task(
        annotator="synth",
        user_id="U015",
        instruction="Following Harper King's Q3 2024 performance review, her manager is creating a formal development plan for her to transition into a 'Product Marketing Specialist' role. First, find Harper King's skill gap analysis for this target role. Then, assign the two courses recommended in the analysis. After assigning the courses, find her performance review workflow and update the 'Development Plan' stage to 'Completed'. Finally, find her team and add an entry to their training log: 'Harper King enrolled in courses for Product Marketing transition.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper King"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="get_performance_review",
                kwargs={"user_id": "U305", "period": "Q3 2024"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T004",
                    "entry": "Harper King enrolled in courses for Product Marketing transition.",
                },
            ),
        ],
        outputs=[],
    ),
    # 16 - EXPERT COMPLEXITY (14 edges) - DEVOPS SECURITY DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U016",
        instruction="Following Harper King's 'Q3 2024' performance review, create her formal development plan. First, find her performance review workflow for that period. In the workflow, update the 'Goal Setting' stage to 'Completed' and the 'Development Plan' stage to 'In Progress'. Next, enroll her in two specific courses: 'Agile Product Management' and 'Data Visualization with Tableau'. Finally, find an available mentor with expertise in 'Policy' and 'Design' and link them to her.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper King"},
            ),
            Action(
                name="get_performance_review",
                kwargs={"user_id": "U305", "period": "Q3 2024"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Goal Setting",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="find_course_by_name",
                kwargs={"name": "Agile Product Management"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="find_course_by_name",
                kwargs={"name": "Data Visualization with Tableau"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Policy", "Design"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U305", "mentor_id": "M100"},
            ),
        ],
        outputs=['{\n  "success": "Mentor M100 -> U305"\n}'],
    ),
    # 17 - REPLACED
    Task(
        annotator="synth",
        user_id="U017",
        instruction="Manager David Adams is actioning the 'Succession Planning' workflow for candidate Chloe Scott. First, find the workflow and update two stages: set 'Candidate Identification' to 'Completed' and 'Skills Assessment' to 'In Progress'. Next, find Chloe's application for the 'UX Design Lead' job to review her skill gaps. Based on her primary gap, 'Design Operations', search for relevant courses. Since no course is found, find an available mentor with 'Design' expertise and link them to Chloe. Finally, set a new active performance goal for her: goal_id 'G307-2', type 'Leadership', description 'Shadow a Design Lead on one project and present findings.', with a last updated date of '2025-07-10'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Chloe Scott"},
            ),
            Action(
                name="find_workflow",
                kwargs={"employee_id": "U307", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Candidate Identification",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Skills Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "UX Design Lead"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U307", "job_id": "J002"},
            ),
            Action(
                name="get_job_application",
                kwargs={"application_id": "APP005"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "Design Operations"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U307", "mentor_id": "M100"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U307",
                    "goal": {
                        "goal_id": "G307-2",
                        "goal_type": "Leadership",
                        "goal_description": "Shadow a Design Lead on one project and present findings.",
                        "status": "Active",
                        "last_updated": "2025-07-10",
                    },
                },
            ),
        ],
        outputs=[],
    ),
    # 18 - EXPERT COMPLEXITY (15 edges) - PRODUCT MARKETING UPSKILLING
    Task(
        annotator="synth",
        user_id="U018",
        instruction="To formalize his career transition to 'UX Writer', Henry Hassan needs a development plan. First, find his skill gap analysis for the target role. Based on the primary 'UX Writing' gap, search for a relevant course. Since no course is found, find an available mentor with 'Design' expertise and link them to him. Next, update his 'UX Writing' skill proficiency to 'Intermediate' to reflect the start of his development. Finally, set a new active goal with ID 'G308-2', type 'Skill Mastery', description 'Rewrite documentation for one flagship feature using UX writing principles.', with a last updated date of '2025-10-05', and log this action to his team's training log with the following entry: 'Henry Hassan assigned mentor for UX Writing development.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Henry Hassan"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "UX Writing"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U308", "mentor_id": "M100"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U308",
                    "skill": "UX Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U308",
                    "goal": {
                        "goal_id": "G308-2",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Rewrite documentation for one flagship feature using UX writing principles.",
                        "status": "Active",
                        "last_updated": "2025-10-05",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U308"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T006",
                    "entry": "Henry Hassan assigned mentor for UX Writing development.",
                },
            ),
        ],
        outputs=[
            '{"success": "Mentor M100 -> U308"}',
            '{"success": "U308 UX Writing -> Intermediate"}',
            '{"success": "Goal set for U308"}',
            '{"success": "Log entry added for T006"}',
        ],
    ),
    # 19 - REPLACED
    Task(
        annotator="synth",
        user_id="U019",
        instruction="To support Logan Garcia's goal of pivoting to a 'Cloud Security Compliance Specialist' role, please create a development plan. First, find the job posting for this role to identify key skills. Based on the 'Policy Writing' requirement, search for and assign the relevant course. Then, check his current certifications. Next, find an available mentor with 'Policy' expertise and link them. Finally, update his 'Policy Writing' skill proficiency to 'Intermediate' to reflect his ongoing development, and add an entry to his team's training log: 'Logan Garcia enrolled in Policy Writing course for cloud compliance path.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Logan Garcia"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Cloud Security Compliance Specialist"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "Policy Writing"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U303", "course_id": "C1007"},
            ),
            Action(
                name="get_user_certification",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Policy"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U303", "mentor_id": "M100"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U303",
                    "skill": "Policy Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T005",
                    "entry": "Logan Garcia enrolled in Policy Writing course for cloud compliance path.",
                },
            ),
        ],
        outputs=[],
    ),
    # 20 - EXPERT COMPLEXITY (15 edges) - ANALYTICS SKILLS DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U020",
        instruction="Henry Hassan is formalizing his career transition to 'UX Writer'. First, find his skill gap analysis for the role. Since no courses are available for his 'UX Writing' and 'Information Architecture' gaps, find an available mentor with 'Design' expertise and link them. Then, set two separate performance active goals for Skill Mastery to address his gaps: one with ID 'G308-3' for 'UX Writing' with description 'Rewrite documentation for one flagship feature using UX writing principles.', and another with ID 'G308-4' for 'Information Architecture' with description 'Develop a new site map for the help center.', both with a last updated date of '2025-11-25'. Finally, log this action to his team's training log with the following entry: 'Henry Hassan assigned mentor and goals for UX Writer transition.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Henry Hassan"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U308", "mentor_id": "M100"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U308",
                    "goal": {
                        "goal_id": "G308-3",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Rewrite documentation for one flagship feature using UX writing principles.",
                        "status": "Active",
                        "last_updated": "2025-11-25",
                    },
                },
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U308",
                    "goal": {
                        "goal_id": "G308-4",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Develop a new site map for the help center.",
                        "status": "Active",
                        "last_updated": "2025-11-25",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U308"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T006",
                    "entry": "Henry Hassan assigned mentor and goals for UX Writer transition.",
                },
            ),
        ],
        outputs=[
            '{"success": "Mentor M100 -> U308"}',
            '{"success": "Goal set for U308"}',
            '{"success": "Log entry added for T006"}',
        ],
    ),
    # 21 - REPLACED
    Task(
        annotator="synth",
        user_id="U021",
        instruction="Create a development plan for Mason Desai's transition to 'Backend Tech Lead'. First, analyze his skill gaps for the role. Based on the 'Team Leadership' gap, assign him the correct course. Then, find an available mentor with 'Engineering' and 'Career Growth' expertise and link them. Finally, set a new active performance goal with ID 'G312-2', type 'Role Transition', description 'Lead one microservices redesign project and complete leadership training.', and a last updated date of '2025-07-15'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Mason Desai"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U312", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U312", "mentor_id": "M101"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U312",
                    "goal": {
                        "goal_id": "G312-2",
                        "goal_type": "Role Transition",
                        "goal_description": "Lead one microservices redesign project and complete leadership training.",
                        "status": "Active",
                        "last_updated": "2025-07-15",
                    },
                },
            ),
        ],
        outputs=[
            '{"success": "U312 enrolled in C1004"}',
            '{"success": "Mentor M101 -> U312"}',
            '{"success": "Goal set for U312"}',
        ],
    ),
    # 22 - REPLACED
    Task(
        annotator="synth",
        user_id="U022",
        instruction="Ava Nguyen is starting her development plan to become a 'Clinical Analytics Lead'. First, find her skill gaps for this role. Based on the primary gap, 'Python', search for a suitable course and enroll her. Then, check her existing certifications. Next, find her 'Internal Promotion Process' workflow and update the 'Development Plan' stage to 'In Progress'. After that, find an available mentor with 'Leadership' expertise and link them. Finally, add an entry to her team's training log: 'Ava Nguyen initiated Python training for career pathing.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "Python"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="get_user_certification",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="find_workflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Internal Promotion Process",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen initiated Python training for career pathing.",
                },
            ),
        ],
        outputs=[
            '{"success": "U302 enrolled in C1001"}',
            '{"success": "Development Plan -> In Progress"}',
            '{"success": "Mentor M102 -> U302"}',
            '{"success": "Log entry added for T001"}',
        ],
    ),
    # 23 - REPLACED
    Task(
        annotator="synth",
        user_id="U023",
        instruction="To formalize Harper King's transition to 'Product Marketing Specialist', execute the following development plan. First, find her skill gap analysis for the target role. Based on the primary gap, 'Product Marketing', assign the correct course according to policy. Then, check her overall course progress. Next, find an available mentor with 'Career Growth' expertise and link them. After that, find her 'Performance Management' workflow and update the 'Development Plan' stage to 'Completed'. Finally, add an entry to her team's training log: 'Harper King development plan for PMM transition formalized.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper King"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="get_user_course_progress",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U305", "mentor_id": "M101"},
            ),
            Action(
                name="find_workflow",
                kwargs={
                    "employee_id": "U305",
                    "workflow_name": "Performance Management",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T004",
                    "entry": "Harper King development plan for PMM transition formalized.",
                },
            ),
        ],
        outputs=[
            '{"success": "U305 enrolled in C1006"}',
            '{"success": "Mentor M101 -> U305"}',
            '{"success": "Development Plan -> Completed"}',
            '{"success": "Log entry added for T004"}',
        ],
    ),
    # 24 - EXPERT COMPLEXITY (13 edges) - UX DESIGN SKILLS DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U024",
        instruction="To support Jack Wang's transition to 'Director of Data Science', create a formal development plan. First, find his skill gap analysis for the role. Based on the identified gaps, assign him the courses for 'Machine Learning' and 'Team Leadership'. Next, find an available mentor with 'Career Growth' expertise and link them. Finally, set a new active goal with ID 'G301-3', type 'Role Transition', description 'Complete Machine Learning and Leadership courses for Director transition.', with a last updated date of '2025-10-15', and log this action to his team's training log with the following entry: 'Jack Wang assigned courses and mentor for Director transition.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Jack Wang"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U301", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U301", "mentor_id": "M101"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U301",
                    "goal": {
                        "goal_id": "G301-3",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete Machine Learning and Leadership courses for Director transition.",
                        "status": "Active",
                        "last_updated": "2025-10-15",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U301"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Jack Wang assigned courses and mentor for Director transition.",
                },
            ),
        ],
        outputs=[
            '{"success": "U301 enrolled in C1005"}',
            '{"success": "U301 enrolled in C1004"}',
            '{"success": "Mentor M101 -> U301"}',
            '{"success": "Goal set for U301"}',
            '{"success": "Log entry added for T001"}',
        ],
    ),
    # 25 - REPLACED
    Task(
        annotator="synth",
        user_id="U025",
        instruction="Hiring manager Mason Desai is processing the application from Alexander Adams for the 'DevOps Engineer' position. He considers him a strong candidate. First, find the application and shortlist Alexander for the job. Then, update the application status to 'Interview Scheduled'. To address a minor skill gap pre-interview, find an available mentor with 'Engineering' expertise and link them to Alexander. Finally, find Alexander's team and add an entry to their training log: 'Alexander Adams assigned mentor for Terraform skill development pre-interview.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "DevOps Engineer"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U306", "job_id": "J003"},
            ),
            Action(
                name="shortlist_candidate",
                kwargs={"job_id": "J003", "candidate_id": "U306"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "status": "Interview Scheduled"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Engineering"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U306", "mentor_id": "M101"},
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T003",
                    "entry": "Alexander Adams assigned mentor for Terraform skill development pre-interview.",
                },
            ),
        ],
        outputs=[
            '{"success": "U306 shortlisted for J003"}',
            '{"success": "APP007 status Interview Scheduled"}',
            '{"success": "Mentor M101 -> U306"}',
            '{"success": "Log entry added for T003"}',
        ],
    ),
    # 26 - HIGH COMPLEXITY (11 edges) - COMPLIANCE TECHNOLOGY ADVANCEMENT
    Task(
        annotator="synth",
        user_id="U026",
        instruction="As part of the formal 'Skills Development Program' program, L&D is actioning the development plan for participant Ava Nguyen. First, find the program's workflow. Then, update the 'Training Delivery' stage to 'Completed' and 'Progress Assessment' to 'In Progress'. Next, assign the two courses specified in the program, 'Advanced Python' and 'Machine Learning Specialization'. Then, link the pre-assigned mentor to her. Finally, set a new active goal with ID 'G302-4', type 'Skill Mastery', description 'Complete Skills Development Program program and apply to one clinical project.', with a last updated date of '2025-10-20', and log this action to her team's training log with the following entry: 'Ava Nguyen development plan actioned for Skills Development Program program.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="find_workflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Skills Development Program",
                },
            ),
            Action(
                name="get_workflow_details",
                kwargs={"workflow_id": "WF005"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Training Delivery",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Progress Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-4",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Complete Skills Development Program and apply to one clinical project.",
                        "status": "Active",
                        "last_updated": "2025-10-20",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen development plan actioned for Skills Development Program.",
                },
            ),
        ],
        outputs=[
            '{"success": "Training Delivery -> Completed"}',
            '{"success": "Progress Assessment -> In Progress"}',
            '{"success": "U302 enrolled in C1001"}',
            '{"success": "U302 enrolled in C1005"}',
            '{"success": "Mentor M102 -> U302"}',
            '{"success": "Goal set for U302"}',
            '{"success": "Log entry added for T001"}',
        ],
    ),
    # 27 - REPLACED
    Task(
        annotator="synth",
        user_id="U027",
        instruction="As part of the 'Skills Development Program' for the new 'People Analytics Platform' project, L&D needs to advance Harper Bennett's training. First, find the program's workflow for Harper. Then, update the 'Training Delivery' stage to 'Completed' and the 'Progress Assessment' stage to 'In Progress'. Next, check her skill gap for the 'People Analytics Lead' role and assign the course for the identified 'Statistical Modeling' gap. Also, check her existing certifications. Finally, find an available mentor with 'Leadership' expertise, link them to her, and add an entry to her team's training log: 'Harper Bennett assigned ML course for People Analytics Platform project.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="find_workflow",
                kwargs={
                    "employee_id": "U310",
                    "workflow_name": "Skills Development Program",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Training Delivery",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Progress Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="get_user_certification",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T008",
                    "entry": "Harper Bennett assigned ML course for People Analytics Platform project.",
                },
            ),
        ],
        outputs=[
            '{"success": "Training Delivery -> Completed"}',
            '{"success": "Progress Assessment -> In Progress"}',
            '{"success": "U310 enrolled in C1005"}',
            '{"success": "Mentor M102 -> U310"}',
            '{"success": "Log entry added for T008"}',
        ],
    ),
    # 28 - EXPERT COMPLEXITY (14 edges) - CONTENT WRITING CAREER GROWTH
    Task(
        annotator="synth",
        user_id="U028",
        instruction="Manager Jack Wang is creating a development plan for his own transition to 'Director of Data Science'. First, analyze his skill gaps for the role. Based on the 'Machine Learning' gap, assign him the correct course. Then, find an available mentor with 'Leadership' and 'Policy' expertise and link them. Next, update his 'Machine Learning' skill proficiency to 'Intermediate'. Finally, set a new active goal with ID 'G301-3', type 'Role Transition', description 'Complete Machine Learning course and lead one predictive modeling initiative.', with a last updated date of '2025-10-25', and log this action to his team's training log with the following log: 'Jack Wang assigned ML course and mentor for Director transition.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Jack Wang"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership", "Policy"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U301", "mentor_id": "M102"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U301",
                    "skill": "Machine Learning",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U301",
                    "goal": {
                        "goal_id": "G301-3",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete Machine Learning course and lead one predictive modeling initiative.",
                        "status": "Active",
                        "last_updated": "2025-10-25",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U301"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Jack Wang assigned ML course and mentor for Director transition.",
                },
            ),
        ],
        outputs=[
            '{"success": "U301 enrolled in C1005"}',
            '{"success": "Mentor M102 -> U301"}',
            '{"success": "U301 Machine Learning -> Intermediate"}',
            '{"success": "Goal set for U301"}',
            '{"success": "Log entry added for T001"}',
        ],
    ),
    # 29 - REPLACED
    Task(
        annotator="synth",
        user_id="U029",
        instruction="Hiring manager Jack Wang is advancing Ava Nguyen's application for the 'Senior Data Scientist' role. First, find her application and update its status to 'Interview Scheduled'. Then, shortlist her for the job. To prepare her for the interview, find an available mentor with 'Leadership' expertise and link them to her. Finally, find her team and add an entry to their training log: 'Ava Nguyen assigned mentor for leadership development pre-interview.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "status": "Interview Scheduled"},
            ),
            Action(
                name="shortlist_candidate",
                kwargs={"job_id": "J001", "candidate_id": "U302"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen assigned mentor for leadership development pre-interview.",
                },
            ),
        ],
        outputs=[
            '{"success": "APP001 status Interview Scheduled"}',
            '{"success": "U302 shortlisted for J001"}',
            '{"success": "Mentor M102 -> U302"}',
            '{"success": "Log entry added for T001"}',
        ],
    ),
    # 30 - EXPERT COMPLEXITY (15 edges) - MARKETING STRATEGY DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U030",
        instruction="L&D Specialist Owen Walker is beginning his project to 'Prototype an AR-based onboarding module'. To formalize his development, first find his user profile. Then, check his progress on the 'Project Management Professional (PMP)' course to confirm his enrollment. Next, find an available mentor with 'Engineering' expertise to support the technical side of the project and link them to him. After that, update his 'AR/VR Training' skill proficiency to 'Beginner'. Finally, set a new active goal with ID 'G309-2', type 'Project', description 'Complete PMP certification and deliver AR onboarding module prototype by Q2 2026.', with a last updated date of '2025-11-05', and log this action to the L&D team's training log with the following entry: 'Owen Walker development plan initiated for AR onboarding project.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Owen Walker"},
            ),
            Action(
                name="find_course_by_name",
                kwargs={"name": "Project Management Professional (PMP)"},
            ),
            Action(
                name="get_course_progress",
                kwargs={"user_id": "U309", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Engineering"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U309", "mentor_id": "M101"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U309",
                    "skill": "AR/VR Training",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U309",
                    "goal": {
                        "goal_id": "G309-2",
                        "goal_type": "Project",
                        "goal_description": "Complete PMP certification and deliver AR onboarding module prototype by Q2 2026.",
                        "status": "Active",
                        "last_updated": "2025-11-05",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U309"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T007",
                    "entry": "Owen Walker development plan initiated for AR onboarding project.",
                },
            ),
        ],
        outputs=[
            '{"success": "Mentor M101 -> U309"}',
            '{"success": "U309 AR/VR Training -> Beginner"}',
            '{"success": "Goal set for U309"}',
            '{"success": "Log entry added for T007"}',
        ],
    ),
    # 31 - REPLACED
    Task(
        annotator="synth",
        user_id="U031",
        instruction="To formalize Harper King's transition to 'Product Marketing Specialist', create a full development plan. First, find her skill gap analysis for the role. Then, assign courses for both identified gaps: 'Product Marketing' and 'Data Analytics'. Next, find an available mentor with 'Career Growth' expertise and link them to her. After that, find her 'Performance Management' workflow and update the 'Development Plan' stage to 'Completed'. Finally, set a new active goal with ID 'G305-2', type 'Skill Mastery', description 'Complete Product Marketing and Data Analytics courses.', and a last updated date of '2025-07-20'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper King"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U305", "mentor_id": "M101"},
            ),
            Action(
                name="find_workflow",
                kwargs={
                    "employee_id": "U305",
                    "workflow_name": "Performance Management",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U305",
                    "goal": {
                        "goal_id": "G305-2",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Complete Product Marketing and Data Analytics courses.",
                        "status": "Active",
                        "last_updated": "2025-07-20",
                    },
                },
            ),
        ],
        outputs=[
            '{"success": "U305 enrolled in C1006"}',
            '{"success": "U305 enrolled in C1003"}',
            '{"success": "Mentor M101 -> U305"}',
            '{"success": "Development Plan -> Completed"}',
            '{"success": "Goal set for U305"}',
        ],
    ),
    # 32 - EXPERT COMPLEXITY (14 edges) - INFRASTRUCTURE AUTOMATION DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U306",
        instruction="Following a review of Harper Bennett's application for the 'Senior Data Scientist' role, HR has decided to place her on a development track for a future data analyst position. First, find her application and update its status to 'Rejected - Development Plan Initiated'. Then, using the skill gaps noted in the application, assign her the courses for 'Machine Learning' and 'Python'. Next, find an available mentor with 'Career Growth' expertise and link them to her. Finally, set a new active goal with ID 'G310-4', type 'Skill Mastery', description 'Complete ML and Python courses for future data analyst role.', with a last updated date of '2025-11-10', and log this action to her team's training log with the following message: 'Harper Bennett placed on development track for future data analyst roles.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U310", "job_id": "J001"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP002",
                    "status": "Rejected - Development Plan Initiated",
                },
            ),
            Action(
                name="get_job_application",
                kwargs={"application_id": "APP002"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1001"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U310", "mentor_id": "M101"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U310",
                    "goal": {
                        "goal_id": "G310-4",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Complete ML and Python courses for future data analyst role.",
                        "status": "Active",
                        "last_updated": "2025-11-10",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T008",
                    "entry": "Harper Bennett placed on development track for future data analyst roles.",
                },
            ),
        ],
        outputs=[
            '{"success": "APP002 status Rejected - Development Plan Initiated"}',
            '{"success": "U310 enrolled in C1005"}',
            '{"success": "U310 enrolled in C1001"}',
            '{"success": "Mentor M101 -> U310"}',
            '{"success": "Goal set for U310"}',
            '{"success": "Log entry added for T008"}',
        ],
    ),
    # 33 - REPLACED
    Task(
        annotator="synth",
        user_id="U033",
        instruction="For the upcoming 'Microservices Migration' project, senior engineer Mason Desai needs to upskill his teammate Alexander Adams. First, find Alexander and analyze his skill gap for the 'Staff SRE' role. Based on the 'Technical Leadership' gap, assign him the correct course. Then, check his progress on that specific course to verify his status. Next, find an available mentor with 'Engineering' and 'Career Growth' expertise and link them. Finally, update Alexander's 'Team Leadership' skill proficiency to 'Beginner' and add an entry to the Engineering Team's training log: 'Alexander Adams assigned leadership training for Microservices Migration project.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U306", "course_id": "C1004"},
            ),
            Action(
                name="get_course_progress",
                kwargs={"user_id": "U306", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U306", "mentor_id": "M101"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U306",
                    "skill": "Team Leadership",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T003",
                    "entry": "Alexander Adams assigned leadership training for Microservices Migration project.",
                },
            ),
        ],
        outputs=[
            '{"success": "U306 enrolled in C1004"}',
            '{"success": "Mentor M101 -> U306"}',
            '{"success": "U306 Team Leadership -> Beginner"}',
            '{"success": "Log entry added for T003"}',
        ],
    ),
    # 34 - HIGH COMPLEXITY (7 edges) - ACCESSIBILITY EXPERTISE DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U307",
        instruction="To support Logan Garcia's goal of earning the 'AWS Security Specialty' certification and moving into a 'Cloud Security Compliance Specialist' role, please formalize his development plan. First, find the job posting for the target role. Based on the 'Policy Writing' requirement, search for and assign the relevant course. Next, update his 'Policy Writing' skill proficiency to 'Intermediate'. Then, find an available mentor with both 'Policy' and 'Leadership' expertise and link them. Finally, set a new active goal with ID 'G303-3', type 'Certification', description 'Complete foundational policy course and achieve AWS Security Specialty certification.', with a last updated date of '2025-11-12', and log this action to his team's training log with the following entry: 'Logan Garcia assigned course and mentor for AWS Security certification path.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Logan Garcia"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Cloud Security Compliance Specialist"},
            ),
            Action(
                name="search_courses",
                kwargs={"skill": "Policy Writing"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U303", "course_id": "C1007"},
            ),
            Action(
                name="update_skill_proficiency",
                kwargs={
                    "user_id": "U303",
                    "skill": "Policy Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Policy", "Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U303", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-3",
                        "goal_type": "Certification",
                        "goal_description": "Complete foundational policy course and achieve AWS Security Specialty certification.",
                        "status": "Active",
                        "last_updated": "2025-11-12",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T005",
                    "entry": "Logan Garcia assigned course and mentor for AWS Security certification path.",
                },
            ),
        ],
        outputs=[
            '{"success": "U303 enrolled in C1007"}',
            '{"success": "U303 Policy Writing -> Intermediate"}',
            '{"success": "Mentor M102 -> U303"}',
            '{"success": "Goal set for U303"}',
            '{"success": "Log entry added for T005"}',
        ],
    ),
    # 35 - EXPERT COMPLEXITY (10 edges) - DESIGNOPS LEAD DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U035",
        instruction="Hiring manager Jack Wang has reviewed Harper Bennett's application for the 'Senior Data Scientist' role. He is rejecting her for this opening but wants to create a development plan for a future role. First, find her application and update its status to 'Rejected - Future Consideration'. Then, based on the 'Machine Learning' and 'Python' skill gaps noted in her application, assign her the two corresponding courses. Next, find an available mentor with 'Leadership' expertise and link them to her. Finally, set a new active goal with ID 'G310-2', type 'Role Transition', description 'Complete ML and Python training for future Data Scientist opportunities.', with a last updated date of '2025-09-05', and log this action to her team's training log with the entry 'Harper Bennett placed on development track for future Data Scientist roles.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U310", "job_id": "J001"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP002",
                    "status": "Rejected - Future Consideration",
                },
            ),
            Action(
                name="get_job_application",
                kwargs={"application_id": "APP002"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U310", "course_id": "C1001"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U310",
                    "goal": {
                        "goal_id": "G310-2",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete ML and Python training for future Data Scientist opportunities.",
                        "status": "Active",
                        "last_updated": "2025-09-05",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T008",
                    "entry": "Harper Bennett placed on development track for future Data Scientist roles.",
                },
            ),
        ],
        outputs=[
            '{"success": "APP002 status Rejected - Future Consideration"}',
            '{"success": "U310 enrolled in C1005"}',
            '{"success": "U310 enrolled in C1001"}',
            '{"success": "Mentor M102 -> U310"}',
            '{"success": "Goal set for U310"}',
            '{"success": "Log entry added for T008"}',
        ],
    ),
    # 36 - REPLACED
    Task(
        annotator="synth",
        user_id="U036",
        instruction="Hiring manager Jack Wang is impressed with Ava Nguyen's application for the 'Senior Data Scientist' role and wants to move her forward. First, find her application and update its status to 'Interview Scheduled'. Then, shortlist her for the job. To proactively address the 'Machine Learning' skill gap noted in her application, assign her the correct course based on policy. Also, find an available mentor with 'Leadership' expertise and link them to her. Finally, add an entry to her team's training log: 'Ava Nguyen assigned ML course and mentor as part of interview process for Senior Data Scientist role.'",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "status": "Interview Scheduled"},
            ),
            Action(
                name="shortlist_candidate",
                kwargs={"job_id": "J001", "candidate_id": "U302"},
            ),
            Action(
                name="get_job_application",
                kwargs={"application_id": "APP001"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen assigned ML course and mentor as part of interview process for Senior Data Scientist role.",
                },
            ),
        ],
        outputs=[
            '{"success": "APP001 status Interview Scheduled"}',
            '{"success": "U302 shortlisted for J001"}',
            '{"success": "U302 enrolled in C1005"}',
            '{"success": "Mentor M102 -> U302"}',
            '{"success": "Log entry added for T001"}',
        ],
    ),
    # 37 - EXPERT COMPLEXITY 13 edges - COMPREHENSIVE UX WRITING DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U037",
        instruction="To prepare Mason Desai to lead the 'backend microservices redesign' project, please formalize his development plan. First, find his skill gap analysis for the 'Backend Tech Lead' role, which shows gaps in 'Systems Design', 'Team Leadership', and 'Kotlin'. Assign him the correct course for the 'Team Leadership' gap. For the technical gaps, find an available mentor with 'Engineering' and 'Career Growth' expertise and link them. Finally, set a new active goal with ID 'G312-4', type 'Project', description 'Lead the backend microservices redesign by enhancing Systems Design and Kotlin skills.', with a last updated date of '2025-11-15', and log this action to his team's training log with the following entry: 'Mason Desai assigned course and mentor for microservices redesign project.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Mason Desai"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U312", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U312", "mentor_id": "M101"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U312",
                    "goal": {
                        "goal_id": "G312-4",
                        "goal_type": "Project",
                        "goal_description": "Lead the backend microservices redesign by enhancing Systems Design and Kotlin skills.",
                        "status": "Active",
                        "last_updated": "2025-11-15",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U312"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T003",
                    "entry": "Mason Desai assigned course and mentor for microservices redesign project.",
                },
            ),
        ],
        outputs=[
            '{"success": "U312 enrolled in C1004"}',
            '{"success": "Mentor M101 -> U312"}',
            '{"success": "Goal set for U312"}',
            '{"success": "Log entry added for T003"}',
        ],
    ),
    # 38 - HIGH COMPLEXITY (12 edges) - INFRASTRUCTURE RELIABILITY ENHANCEMENT
    Task(
        annotator="synth",
        user_id="U038",
        instruction="David Adams is formalizing his own development plan to become a 'DesignOps Lead'. First, he wants to review his entire course progress history. After reviewing, he wants to act on his formal skill gap analysis for the role. Based on the 'Stakeholder Alignment' gap, assign the correct leadership course. Then, find an available mentor with 'Leadership' expertise and link them. Finally, set a new active goal with ID 'G304-4', type 'Skill Mastery', description 'Master Design Operations by formalizing two cross-team processes.', with a last updated date of '2025-11-18', and log this action to his team's training log with the following entry: 'David Adams initiated development plan for DesignOps Lead role.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "David Adams"},
            ),
            Action(
                name="get_user_course_progress",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-4",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Master Design Operations by formalizing two cross-team processes.",
                        "status": "Active",
                        "last_updated": "2025-11-18",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T002",
                    "entry": "David Adams initiated development plan for DesignOps Lead role.",
                },
            ),
        ],
        outputs=[
            '{"success": "U304 enrolled in C1004"}',
            '{"success": "Mentor M102 -> U304"}',
            '{"success": "Goal set for U304"}',
            '{"success": "Log entry added for T002"}',
        ],
    ),
    # 39 - EXPERT COMPLEXITY (15 edges) - WRITING TECHNOLOGY ADVANCEMENT
    Task(
        annotator="synth",
        user_id="U039",
        instruction="HR Partner Harper Bennett is actioning the 'Succession Planning' workflow for candidate David Adams. First, find the workflow and update two stages: 'Candidate Identification' to 'Completed' and 'Skills Assessment' to 'In Progress'. Next, find his skill gap analysis for the 'DesignOps Lead' role. Based on his 'Stakeholder Alignment' gap, assign him the correct leadership course. Then, find an available mentor with 'Leadership' expertise and link them. Finally, set a new active goal with ID 'G304-5', type 'Leadership', description 'Complete leadership course and lead stakeholder alignment for one cross-functional project.', with a last updated date of '2025-11-20', and log this action to his team's training log with the following entry: 'David Adams assigned leadership course and mentor as part of succession plan.'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "David Adams"},
            ),
            Action(
                name="find_workflow",
                kwargs={"employee_id": "U304", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Candidate Identification",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Skills Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="get_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-5",
                        "goal_type": "Leadership",
                        "goal_description": "Complete leadership course and lead stakeholder alignment for one cross-functional project.",
                        "status": "Active",
                        "last_updated": "2025-11-20",
                    },
                },
            ),
            Action(
                name="get_user_profile",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="update_team_training_log",
                kwargs={
                    "team_id": "T002",
                    "entry": "David Adams assigned leadership course and mentor as part of succession plan.",
                },
            ),
        ],
        outputs=[
            '{"success": "Candidate Identification -> Completed"}',
            '{"success": "Skills Assessment -> In Progress"}',
            '{"success": "U304 enrolled in C1004"}',
            '{"success": "Mentor M102 -> U304"}',
            '{"success": "Goal set for U304"}',
            '{"success": "Log entry added for T002"}',
        ],
    ),
    # 40 - EXPERT COMPLEXITY (15 edges) - COMPREHENSIVE DEVELOPMENT INITIATIVE
    Task(
        annotator="synth",
        user_id="U040",
        instruction="Hiring manager Jack Wang has decided not to move forward with Ava Nguyen's application for the 'Senior Data Scientist' role at this time, but wants to put her on a formal development track. First, find her application and update its status to 'Rejected - Future Consideration'. Next, find her 'Internal Promotion Process' workflow and update two stages: 'Skills Assessment' to 'Completed' and 'Development Plan' to 'In Progress'. Then, using the 'Machine Learning' gap from her application, assign the correct course. Finally, find an available mentor with 'Leadership' expertise, link them to her, and set a new active goal with ID 'G302-5', type 'Role Transition', description 'Complete ML course and promotion workflow for future Data Scientist role.', with a last updated date of '2025-11-22'.",
        actions=[
            Action(
                name="find_user_by_name",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="find_job_by_title",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="find_application",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP001",
                    "status": "Rejected - Future Consideration",
                },
            ),
            Action(
                name="find_workflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Internal Promotion Process",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Skills Assessment",
                    "status": "Completed",
                },
            ),
            Action(
                name="update_workflow_stage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="get_job_application",
                kwargs={"application_id": "APP001"},
            ),
            Action(
                name="assign_course",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="find_mentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="link_mentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="set_performance_goal",
                kwargs={
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-5",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete ML course and promotion workflow for future Data Scientist role.",
                        "status": "Active",
                        "last_updated": "2025-11-22",
                    },
                },
            ),
        ],
        outputs=[
            '{"success": "APP001 status Rejected - Future Consideration"}',
            '{"success": "Skills Assessment -> Completed"}',
            '{"success": "Development Plan -> In Progress"}',
            '{"success": "U302 enrolled in C1005"}',
            '{"success": "Mentor M102 -> U302"}',
            '{"success": "Goal set for U302"}',
        ],
    ),
]
