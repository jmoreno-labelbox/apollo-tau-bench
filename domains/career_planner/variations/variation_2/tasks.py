from domains.dto import Task, Action

TASKS = [
    # 1 - EXPERT COMPLEXITY (16 edges) DETERMINISTIC SKILL DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U001",
        instruction="As part of the 'Succession Planning' for the 'UX Design Lead' role, HR Partner Alexander Adams is managing the development plan for candidate Michael Rodriguez. Begin by locating the relevant workflow and changing the 'Development Planning' stage to 'In Progress'. Subsequently, identify his skill gap analysis for the 'DesignOps Lead' role. Following the suggested course for his 'Stakeholder Alignment' gap, proceed to enroll him in the training. After that, find a mentor with 'Leadership' expertise who is available and connect them. Lastly, establish a new active goal with ID 'G304-2', type 'Leadership', description 'Complete PMP course and lead stakeholder alignment for one cross-functional project.', with a last updated date of '2025-09-10'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Michael Rodriguez"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={"employee_id": "U304", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Development Planning",
                    "status": "In Progress",
                },
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="For advancement in the UX Writer role, U308 should cultivate Project Management skills. Evaluate skill gaps, search for suitable courses, and register for C1004 (Project Management).",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_id": "U308"}),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(name="GetUserCertification", kwargs={"user_id": "U308"}),
            Action(name="GetUserCourseProgress", kwargs={"user_id": "U308"}),
            Action(
                name="GetPerformanceReview",
                kwargs={"user_id": "U308", "period": "Q3 2024"},
            ),
            Action(name="GetTeamTrainingLog", kwargs={"team_id": "T006"}),
            Action(name="SearchCourses", kwargs={"skill": "Project Management"}),
            Action(name="GetUserCertification", kwargs={"user_id": "U308"}),
            Action(name="GetUserCourseProgress", kwargs={"user_id": "U308"}),
            Action(
                name="GetPerformanceReview",
                kwargs={"user_id": "U308", "period": "Q3 2024"},
            ),
            Action(name="GetTeamTrainingLog", kwargs={"team_id": "T006"}),
            Action(name="GetUserProfile", kwargs={"user_id": "U308"}),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(name="GetUserCertification", kwargs={"user_id": "U308"}),
            Action(name="GetUserCourseProgress", kwargs={"user_id": "U308"}),
            Action(
                name="AssignCourse", kwargs={"user_id": "U308", "course_id": "C1004"}
            ),
        ],
        outputs=["U308 enrolled in C1004"],
    ),
    # 3 - EXPERT COMPLEXITY (15 edges)- COMPREHENSIVE LEADERSHIP DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U003",
        instruction="As part of the 'DevOps Automation' project, team lead Michael Rodriguez is designing a development plan for Robert Thompson. Initially, locate Alexander and verify his current certifications. Afterward, identify his skill gaps for the 'Staff SRE' role. Since there is no course available for his 'Terraform' gap, locate an available mentor with 'Engineering' expertise and connect them. Then, revise his 'Terraform' skill proficiency to 'Beginner'. Lastly, establish a new active goal with ID 'G306-3', type 'Skill Mastery', description 'Achieve Intermediate Terraform proficiency for DevOps Automation project.', with a last updated date of '2025-09-12', and record this action in the Engineering Team’s training log with the note: 'Robert Thompson assigned mentor for Terraform skill development for DevOps Automation project.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Robert Thompson"},
            ),
            Action(
                name="GetUserCertification",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Engineering"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U306", "mentor_id": "M101"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U306",
                    "skill": "Terraform",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T003",
                    "entry": "Robert Thompson assigned mentor for Terraform skill development for DevOps Automation project.",
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
        instruction="To aid his objective of obtaining the 'AWS Security Specialty' certification, David Adams requires a foundational development plan. Begin by reviewing his current certifications. Subsequently, locate the job posting for 'Cloud Security Compliance Specialist' to determine a key foundational skill. Based on the 'Policy Writing' requirement, search for and assign the relevant course. Then, modify his 'Policy Writing' skill proficiency to 'Intermediate'. Next, find an available mentor with 'Policy' expertise and connect them. Finally, create a new active goal with ID 'G303-2', type 'Certification', description 'Complete foundational Policy Writing course for AWS Security certification path.', with a last updated date of '2025-08-20'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "David Adams"},
            ),
            Action(
                name="GetUserCertification",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Cloud Security Compliance Specialist"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "Policy Writing"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U303", "course_id": "C1007"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U303",
                    "skill": "Policy Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Policy"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U303", "mentor_id": "M100"},
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="In order to assist Alexander Adams’s transition into the 'People Analytics Lead' position, handle the creation of a formal development plan. First, locate her skill gap analysis for this role. Using the identified gaps, allocate to her the courses on 'Statistical Modeling' and 'Data Visualization'. Then, locate an available mentor with 'Leadership' expertise and connect them to her. Lastly, initiate a new active goal with ID 'G310-3', type 'Role Transition', description 'Complete statistical modeling and data visualization courses to lead the new People Analytics function.', with a final updated date of '2025-09-20'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1003"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="Overseeing the Marketing Team’s preparation for the 'Product Marketing Launch' project, Ava Nguyen needs to establish her development in data analytics, an important area from her performance review. Initially, fetch the review. Subsequently, find her skill gap analysis for the 'Product Marketing Specialist' role. According to the 'Data Analytics' gap, assign her the recommended course. Locate a mentor possessing 'Career Growth' expertise and connect them to her. Finally, adjust the 'Development Plan' phase in her performance review workflow to 'Completed' and insert an entry into the Marketing Team's training log: 'Ava Nguyen assigned Data Analytics course for Product Marketing Launch project.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetPerformanceReview",
                kwargs={"user_id": "U305", "period": "Q3 2024"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U305", "mentor_id": "M101"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T004",
                    "entry": "Ava Nguyen assigned Data Analytics course for Product Marketing Launch project.",
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
        instruction="A manager is developing a career advancement plan for Michael Rodriguez's progression to 'Backend Tech Lead'. Start by identifying his skill deficiencies for the position. In response to the 'Team Leadership' deficiency, enroll him in the appropriate course. Afterward, find a mentor with expertise in 'Engineering' and 'Career Growth' and pair them. Following that, update his 'Team Leadership' skill level to 'Beginner'. Lastly, create a new active goal with ID 'G312-3', type 'Role Transition', and description 'Complete leadership training and lead one backend redesign initiative.', noting it was last updated on '2025-09-25', and record this activity in his team's training log with the note: 'Michael Rodriguez assigned leadership training and mentor for Backend Tech Lead path.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Michael Rodriguez"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U312", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U312", "mentor_id": "M101"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U312",
                    "skill": "Team Leadership",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U312"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T003",
                    "entry": "Michael Rodriguez assigned leadership training and mentor for Backend Tech Lead path.",
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
        instruction="Hiring manager Ava Nguyen evaluates Harper Bennett's application for the 'Senior Data Scientist' position and opts to place her on a development trajectory. Begin by locating her application and changing its status to 'Rejected - Future Consideration'. Subsequently, access her 'Internal Promotion Process' workflow. Within that workflow, modify the 'Skills Assessment' phase to 'Completed' and advance the 'Development Plan' phase to 'In Progress'. At the same time, assess her skill deficiency for the 'Clinical Analytics Lead' role. Based on the 'Python' skill gap identified, assign her the appropriate course. Finally, identify a mentor with 'Leadership' expertise and connect them to her.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="UpdateApplicationStatus",
                kwargs={
                    "application_id": "APP001",
                    "status": "Rejected - Future Consideration",
                },
            ),
            Action(
                name="FindWorkflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Internal Promotion Process",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Skills Assessment",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
        ],
        outputs=[],
    ),
    # 9 - HIGH COMPLEXITY (13 edges) - BACKEND LEADERSHIP DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U009",
        instruction="HR Partner Alexander Adams is handling the 'Succession Planning' workflow for candidate Michael Rodriguez. Initially, locate the workflow and amend the 'Development Planning' stage to 'In Progress'. Subsequently, locate his skill gap analysis for the 'DesignOps Lead' role. Given his 'Stakeholder Alignment' gap, allocate the correct leadership course to him. Then, identify an available mentor with 'Leadership' expertise and connect them. Lastly, establish a new active goal with ID 'G304-3', type 'Leadership', description 'Complete leadership course and formalize one cross-team process.', with a last updated date of '2025-09-30', and record this action in his team's training log with the entry: 'Michael Rodriguez assigned leadership course and mentor as part of succession plan.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Michael Rodriguez"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={"employee_id": "U304", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Development Planning",
                    "status": "In Progress",
                },
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T002",
                    "entry": "Michael Rodriguez assigned leadership course and mentor as part of succession plan.",
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
        instruction="As the team lead for the Data Analytics Team, Ava Nguyen is coordinating the preparation of Harper Bennett for the upcoming 'Predictive Modeling Initiative'. First, identify Jack's team ID. Next, locate Harper Bennett and assess her skill gap for the 'Clinical Analytics Lead' role. Based on the identified 'Python' gap, assign her the necessary course. Following the assignment, verify her enrollment status for that course. Then, add an entry to the team's training log: 'Harper Bennett assigned Python training for Predictive Modeling project.' Finally, to formally monitor her development, update her proficiency for the 'Python' skill to 'Beginner'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U301"},
            ),
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="GetCourseProgress",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Harper Bennett assigned Python training for Predictive Modeling project.",
                },
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={"user_id": "U302", "skill": "Python", "new_level": "Beginner"},
            ),
        ],
        outputs=[],
    ),
    # 11 - HIGH COMPLEXITY (14 edges) - CLINICAL ANALYTICS PROGRESSION
    Task(
        annotator="synth",
        user_id="U011",
        instruction="In preparation for the 'Predictive Modeling Initiative', it is necessary for team lead Ava Nguyen to enhance Harper Bennett's skills. Begin by locating Ava's application for the 'Senior Data Scientist' position to determine her primary skill deficiency. With the identified gap in 'Machine Learning', enroll her in the appropriate course. Afterward, monitor her advancement in this newly assigned course. Subsequently, identify an accessible mentor with proficiency in 'Leadership' and establish a connection with her. Conclude by updating her proficiency level in 'Machine Learning' to 'Beginner' and recording this update in the Data Analytics Team's training documentation: 'Harper Bennett assigned ML training for Predictive Modeling Initiative.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="GetJobApplication",
                kwargs={"application_id": "APP001"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="GetCourseProgress",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U302",
                    "skill": "Machine Learning",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Harper Bennett assigned ML training for Predictive Modeling Initiative.",
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
        instruction="Director Michael Rodriguez is tasked with readying Alexander Adams for the 'UX Design Lead' position within the framework of 'Succession Planning'. To start, retrieve Alexander Adams's user ID. Following this, navigate to the appropriate workflow to mark the 'Candidate Identification' phase as 'Completed' and set the 'Skills Assessment' phase to 'In Progress'. Next, access her application for the 'UX Design Lead' role to pinpoint her skill deficiencies. With 'Design Operations' as her chief area for improvement, search for suitable training courses. If no relevant course exists, proceed to identify a mentor skilled in 'Design' and connect them with Chloe. Lastly, implement a new active performance goal for her: goal_id 'G307-2', type 'Leadership', description 'Shadow a Design Lead on one project and present findings.', with a last updated date of '2025-07-10'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={"employee_id": "U307", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Candidate Identification",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Skills Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "UX Design Lead"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U307", "job_id": "J002"},
            ),
            Action(
                name="GetJobApplication",
                kwargs={"application_id": "APP005"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "Design Operations"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U307", "mentor_id": "M100"},
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="To aid Alexander Adams in achieving her career aspiration of becoming a 'People Analytics Lead', please construct a formal development plan. Begin by locating her skill gap analysis for this target position. In accordance with the suggestions, allocate her the courses for 'Statistical Modeling' and 'Data Visualization'. Following that, find a mentor available with 'Leadership' expertise and connect them to her. Finally, initiate a new active goal with ID 'G310-3', type 'Role Transition', description 'Complete statistical modeling and data visualization courses to lead the new People Analytics function.', with a last updated date of '2025-09-20'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1003"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="Concerning the new 'AR-based onboarding module' project, L&D lead Logan Garcia needs to enhance team member Owen Walker's skills in analytics. Start by locating Lucas and reviewing his existing certifications. Subsequently, search and assign him a 'Tableau' course. Next, modify his 'Tableau' skill proficiency to 'Beginner'. Then, identify an available mentor with 'Career Growth' expertise and establish a connection. Lastly, create a new active goal with ID 'G311-2', type 'Skill Mastery', description 'Apply data visualization skills to measure the effectiveness of the new AR onboarding module.', with a last updated date of '2025-10-01', and register this action to the L&D team's training log with the following note: 'Owen Walker assigned data visualization training for AR/VR project analytics.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Owen Walker"},
            ),
            Action(
                name="GetUserCertification",
                kwargs={"user_id": "U311"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "Tableau"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U311", "course_id": "C1003"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U311",
                    "skill": "Tableau",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U311", "mentor_id": "M101"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U311"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T007",
                    "entry": "Owen Walker assigned data visualization training for AR/VR project analytics.",
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
        instruction="In light of Ava Nguyen's Q3 2024 performance review, her manager is developing a structured development plan for her to move into a 'Product Marketing Specialist' role. Start by locating Ava Nguyen's skill gap analysis for this intended position. Then, enroll her in the two courses suggested within the analysis. After assigning the courses, locate her performance review workflow and mark the 'Development Plan' stage as 'Completed'. Lastly, access her team and insert a note into their training log: 'Ava Nguyen enrolled in courses for Product Marketing transition.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="GetPerformanceReview",
                kwargs={"user_id": "U305", "period": "Q3 2024"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T004",
                    "entry": "Ava Nguyen enrolled in courses for Product Marketing transition.",
                },
            ),
        ],
        outputs=[],
    ),
    # 16 - EXPERT COMPLEXITY (14 edges) - DEVOPS SECURITY DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U016",
        instruction="Considering Ava Nguyen's 'Q3 2024' performance evaluation, coordinate the creation of her formal development plan. Begin by accessing her performance review workflow for that timeframe. Within this workflow, update the 'Goal Setting' stage to 'Completed' and set the 'Development Plan' stage to 'In Progress'. Subsequently, register her in two designated courses: 'Agile Product Management' and 'Data Visualization with Tableau'. Conclusively, find a mentor skilled in 'Policy' and 'Design' and connect them with her.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetPerformanceReview",
                kwargs={"user_id": "U305", "period": "Q3 2024"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Goal Setting",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="FindCourseByName",
                kwargs={"name": "Agile Product Management"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="FindCourseByName",
                kwargs={"name": "Data Visualization with Tableau"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Policy", "Design"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U305", "mentor_id": "M100"},
            ),
        ],
        outputs=['{\n  "success": "Mentor M100 -> U305"\n}'],
    ),
    # 17 - REPLACED
    Task(
        annotator="synth",
        user_id="U017",
        instruction="Michael Rodriguez, as the manager, is overseeing the 'Succession Planning' procedure for candidate Alexander Adams. Begin by locating the workflow and modifying two stages: change 'Candidate Identification' to 'Completed' and 'Skills Assessment' to 'In Progress'. Subsequently, access Chloe's application for the 'UX Design Lead' position to examine her skill deficiencies. Targeting her main gap, 'Design Operations', search for applicable courses. As no course is located, identify a mentor proficient in 'Design' and assign them to Chloe. Finally, introduce a fresh active performance goal for her: goal_id 'G307-2', type 'Leadership', description 'Shadow a Design Lead on one project and present findings.', with a last updated date of '2025-07-10'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={"employee_id": "U307", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Candidate Identification",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Skills Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "UX Design Lead"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U307", "job_id": "J002"},
            ),
            Action(
                name="GetJobApplication",
                kwargs={"application_id": "APP005"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "Design Operations"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U307", "mentor_id": "M100"},
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="Emily Johnson requires a development strategy to transition formally to 'UX Writer'. Begin by discovering his skill gap evaluation related to the intended role. Based on the principal 'UX Writing' gap, search for a suitable course. With no course available, find a mentor who specializes in 'Design' and link them to him. Next, amend his 'UX Writing' skill level to 'Intermediate' to indicate the commencement of his development. Conclusively, establish a new active goal with ID 'G308-2', type 'Skill Mastery', description 'Rewrite documentation for one flagship feature using UX writing principles.', with a last updated date of '2025-10-05', and document this activity in his team's training record with the notation: 'Emily Johnson assigned mentor for UX Writing development.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Emily Johnson"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "UX Writing"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U308", "mentor_id": "M100"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U308",
                    "skill": "UX Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U308"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T006",
                    "entry": "Emily Johnson assigned mentor for UX Writing development.",
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
        instruction="Please initiate a development plan to assist David Adams in shifting to a 'Cloud Security Compliance Specialist' position. Begin by locating the job listing for this role to pinpoint essential skills. Following the 'Policy Writing' requirement, locate and assign the relevant course. After that, verify his existing certifications. Proceed to identify an accessible mentor with 'Policy' expertise and connect them. Lastly, modify his 'Policy Writing' skill proficiency to 'Intermediate' to indicate his progress, and document in his team's training log: 'David Adams enrolled in Policy Writing course for cloud compliance path.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "David Adams"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Cloud Security Compliance Specialist"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "Policy Writing"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U303", "course_id": "C1007"},
            ),
            Action(
                name="GetUserCertification",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Policy"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U303", "mentor_id": "M100"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U303",
                    "skill": "Policy Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T005",
                    "entry": "David Adams enrolled in Policy Writing course for cloud compliance path.",
                },
            ),
        ],
        outputs=[],
    ),
    # 20 - EXPERT COMPLEXITY (15 edges) - ANALYTICS SKILLS DEVELOPMENT
    Task(
        annotator="synth",
        user_id="U020",
        instruction="Emily Johnson is solidifying his career move to 'UX Writer'. Start by retrieving his skill gap analysis for the position. As there are no available courses for his 'UX Writing' and 'Information Architecture' deficiencies, locate an accessible mentor with 'Design' expertise and connect them. Following this, establish two distinct performance active goals for Skill Mastery to tackle his gaps: one labeled ID 'G308-3' for 'UX Writing' with the description 'Rewrite documentation for one flagship feature using UX writing principles.', and another labeled ID 'G308-4' for 'Information Architecture' with the description 'Develop a new site map for the help center.', both with a last updated date of '2025-11-25'. Conclude by documenting this action in his team's training log with the entry: 'Emily Johnson assigned mentor and goals for UX Writer transition.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Emily Johnson"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Design"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U308", "mentor_id": "M100"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U308"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T006",
                    "entry": "Emily Johnson assigned mentor and goals for UX Writer transition.",
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
        instruction="Coordinate the creation of a development plan for Michael Rodriguez's move to 'Backend Tech Lead'. Start by evaluating his skill deficiencies for the position. Considering the 'Team Leadership' gap, assign him to the appropriate course. Next, locate an accessible mentor skilled in 'Engineering' and 'Career Growth' and connect them. Conclude by setting a new active performance goal with ID 'G312-2', type 'Role Transition', description 'Lead one microservices redesign project and complete leadership training.', and ensure the last updated date is '2025-07-15'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Michael Rodriguez"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U312", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U312", "mentor_id": "M101"},
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="Oversee Harper Bennett's initiation of her development plan to become a 'Clinical Analytics Lead'. First, identify her skill deficiencies for this position. Based on the main gap, 'Python', locate and enroll her in a suitable course. Then, review her current certifications. Subsequently, access her 'Internal Promotion Process' workflow and amend the 'Development Plan' stage to 'In Progress'. Following that, find an available mentor with 'Leadership' skills and establish a connection. Finally, append a note to her team's training log: 'Harper Bennett initiated Python training for career pathing.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "Python"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="GetUserCertification",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Internal Promotion Process",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Harper Bennett initiated Python training for career pathing.",
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
        instruction="To finalize Ava Nguyen's transition to 'Product Marketing Specialist', handle the following development plan. Initially, locate her skill gap analysis for the target position. Depending on the primary gap, 'Product Marketing', allocate the appropriate course as per policy. Subsequently, examine her cumulative course progress. Proceed by finding an available mentor with expertise in 'Career Growth' and connect them. Following that, locate her 'Performance Management' workflow and adjust the 'Development Plan' stage to 'Completed'. Conclude by adding a note to her team's training log: 'Ava Nguyen development plan for PMM transition formalized.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="GetUserCourseProgress",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U305", "mentor_id": "M101"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={
                    "employee_id": "U305",
                    "workflow_name": "Performance Management",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U305"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T004",
                    "entry": "Ava Nguyen development plan for PMM transition formalized.",
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
        instruction="To aid Ava Nguyen's transition to 'Director of Data Science', coordinate a formal development plan. Start by finding his skill gap analysis for the role. Based on the identified gaps, enroll him in the courses for 'Machine Learning' and 'Team Leadership'. Subsequently, find an available mentor with expertise in 'Career Growth' and establish a link. Finally, initiate a new active goal with ID 'G301-3', type 'Role Transition', providing the description 'Complete Machine Learning and Leadership courses for Director transition.', last updated on '2025-10-15', and log this action in his team's training log with the entry: 'Ava Nguyen assigned courses and mentor for Director transition.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U301", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U301", "mentor_id": "M101"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U301"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen assigned courses and mentor for Director transition.",
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
        instruction="Hiring manager Michael Rodriguez is handling the application from Robert Thompson for the 'DevOps Engineer' position. He regards him as a strong candidate. Initially, locate the application and shortlist Alexander for the job. Then, update the application status to 'Interview Scheduled'. To address a minor skill gap before the interview, locate an available mentor with 'Engineering' expertise and connect them with Alexander. Lastly, find Alexander's team and log an entry in their training record: 'Robert Thompson assigned mentor for Terraform skill development pre-interview.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Robert Thompson"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "DevOps Engineer"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U306", "job_id": "J003"},
            ),
            Action(
                name="ShortlistCandidate",
                kwargs={"job_id": "J003", "candidate_id": "U306"},
            ),
            Action(
                name="UpdateApplicationStatus",
                kwargs={"application_id": "APP007", "status": "Interview Scheduled"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Engineering"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U306", "mentor_id": "M101"},
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T003",
                    "entry": "Robert Thompson assigned mentor for Terraform skill development pre-interview.",
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
        instruction="Within the formal 'Skills Development Program' program, L&D is coordinating the development plan for participant Harper Bennett. Start by identifying the program's workflow. Then, change the 'Training Delivery' phase to 'Completed' and 'Progress Assessment' to 'In Progress'. Next, assign the two courses specified in the program, 'Advanced Python' and 'Machine Learning Specialization'. After that, connect the pre-assigned mentor with her. Finally, establish a new active goal with ID 'G302-4', type 'Skill Mastery', description 'Complete Skills Development Program program and apply to one clinical project.', with a last updated date of '2025-10-20', and document this action in her team's training log with the following entry: 'Harper Bennett development plan actioned for Skills Development Program program.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Skills Development Program",
                },
            ),
            Action(
                name="GetWorkflowDetails",
                kwargs={"workflow_id": "WF005"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Training Delivery",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Progress Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Harper Bennett development plan actioned for Skills Development Program.",
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
        instruction="As part of the 'Skills Development Program' related to the 'People Analytics Platform' initiative, L&D must progress Alexander Adams's training. Initially, locate the program's workflow concerning Harper. Subsequently, modify the 'Training Delivery' stage to 'Completed' and change the 'Progress Assessment' stage to 'In Progress'. Following that, evaluate her skill gap for the 'People Analytics Lead' position and allocate the course addressing the 'Statistical Modeling' deficiency identified. Additionally, verify her current certifications. Conclusively, identify an available mentor possessing 'Leadership' expertise, connect them to her, and record an entry in her team's training log stating: 'Alexander Adams assigned ML course for People Analytics Platform project.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={
                    "employee_id": "U310",
                    "workflow_name": "Skills Development Program",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Training Delivery",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF005",
                    "stage": "Progress Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="GetUserCertification",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T008",
                    "entry": "Alexander Adams assigned ML course for People Analytics Platform project.",
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
        instruction="Manager Ava Nguyen is preparing a development strategy for his advancement to 'Director of Data Science'. Begin with analyzing his skill deficiencies for the position. Based on the 'Machine Learning' deficiency, assign him the appropriate course. Then, locate an available mentor with expertise in both 'Leadership' and 'Policy' and connect them. After that, upgrade his 'Machine Learning' skill proficiency to 'Intermediate'. Finally, establish a new active goal bearing ID 'G301-3', type 'Role Transition', and a description of 'Complete Machine Learning course and lead one predictive modeling initiative.', with the last updated date as '2025-10-25', and document this action in his team's training log using the log: 'Ava Nguyen assigned ML course and mentor for Director transition.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership", "Policy"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U301", "mentor_id": "M102"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U301",
                    "skill": "Machine Learning",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U301"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Ava Nguyen assigned ML course and mentor for Director transition.",
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
        instruction="Ensure hiring manager Ava Nguyen moves Harper Bennett's application forward for the 'Senior Data Scientist' role. Initially, locate her application and adjust the status to 'Interview Scheduled'. Next, include her in the shortlist for the position. To ready her for the interview, search for a mentor who has 'Leadership' expertise and assign them to her. Lastly, locate her team and record a new entry in their training log: 'Harper Bennett assigned mentor for leadership development pre-interview.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="UpdateApplicationStatus",
                kwargs={"application_id": "APP001", "status": "Interview Scheduled"},
            ),
            Action(
                name="ShortlistCandidate",
                kwargs={"job_id": "J001", "candidate_id": "U302"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Harper Bennett assigned mentor for leadership development pre-interview.",
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
        instruction="L&D Specialist Logan Garcia is embarking on his project to 'Prototype an AR-based onboarding module'. To systematize his development, begin by locating his user profile. Following that, verify his participation in the 'Project Management Professional (PMP)' course to ensure his enrollment status. Subsequently, find a mentor available with 'Engineering' expertise to aid the technical aspects of the project and connect them to him. Thereafter, amend his 'AR/VR Training' skill proficiency level to 'Beginner'. Conclusively, establish a new active goal with ID 'G309-2', type 'Project', description 'Complete PMP certification and deliver AR onboarding module prototype by Q2 2026.', with a last updated date of '2025-11-05', and document this initiative in the L&D team's training log using the following entry: 'Logan Garcia development plan initiated for AR onboarding project.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Logan Garcia"},
            ),
            Action(
                name="FindCourseByName",
                kwargs={"name": "Project Management Professional (PMP)"},
            ),
            Action(
                name="GetCourseProgress",
                kwargs={"user_id": "U309", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Engineering"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U309", "mentor_id": "M101"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U309",
                    "skill": "AR/VR Training",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U309"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T007",
                    "entry": "Logan Garcia development plan initiated for AR onboarding project.",
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
        instruction="To facilitate Ava Nguyen's transition to 'Product Marketing Specialist', prepare a comprehensive development plan. Start by retrieving her skill gap analysis for the position. Afterwards, allocate courses to cover the identified gaps: 'Product Marketing' and 'Data Analytics'. Follow this by finding an available mentor with 'Career Growth' expertise and assigning them to her. Subsequently, locate her 'Performance Management' workflow and change the 'Development Plan' stage to 'Completed'. Lastly, establish a new active goal with ID 'G305-2', type 'Skill Mastery', description 'Complete Product Marketing and Data Analytics courses.', and update the last modified date to '2025-07-20'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Ava Nguyen"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1006"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U305", "course_id": "C1003"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U305", "mentor_id": "M101"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={
                    "employee_id": "U305",
                    "workflow_name": "Performance Management",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF004",
                    "stage": "Development Plan",
                    "status": "Completed",
                },
            ),
            Action(
                name="SetPerformanceGoal",
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
        instruction="After evaluating Alexander Adams's application for the 'Senior Data Scientist' role, HR intends to place her on a development track for an eventual data analyst position. Begin by locating her application and altering its status to 'Rejected - Development Plan Initiated'. Subsequently, based on the skill gaps identified in the application, enroll her in the courses for 'Machine Learning' and 'Python'. Then, find an available mentor with 'Career Growth' expertise to pair with her. Finally, create a new active goal with ID 'G310-4', type 'Skill Mastery', description 'Complete ML and Python courses for future data analyst role.', with a last update on '2025-11-10', and record this action in her team's training log with this message: 'Alexander Adams placed on development track for future data analyst roles.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U310", "job_id": "J001"},
            ),
            Action(
                name="UpdateApplicationStatus",
                kwargs={
                    "application_id": "APP002",
                    "status": "Rejected - Development Plan Initiated",
                },
            ),
            Action(
                name="GetJobApplication",
                kwargs={"application_id": "APP002"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1001"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U310", "mentor_id": "M101"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T008",
                    "entry": "Alexander Adams placed on development track for future data analyst roles.",
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
        instruction="Concerning the 'Microservices Migration' project, senior engineer Michael Rodriguez is required to enhance his teammate Robert Thompson's skills. Initiate by locating Alexander and examining his skill deficiencies related to the 'Staff SRE' position. With respect to the 'Technical Leadership' gap, allocate the appropriate course to him. Afterwards, assess his advancement in that particular course to confirm his status. Subsequently, identify a mentor available with knowledge in 'Engineering' and 'Career Growth' and connect them. Ultimately, amend Alexander's 'Team Leadership' skill proficiency to 'Beginner' and record an entry in the Engineering Team's training log: 'Robert Thompson assigned leadership training for Microservices Migration project.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Robert Thompson"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U306", "course_id": "C1004"},
            ),
            Action(
                name="GetCourseProgress",
                kwargs={"user_id": "U306", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U306", "mentor_id": "M101"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U306",
                    "skill": "Team Leadership",
                    "new_level": "Beginner",
                },
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U306"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T003",
                    "entry": "Robert Thompson assigned leadership training for Microservices Migration project.",
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
        instruction="In order to bolster David Adams's ambition to acquire the 'AWS Security Specialty' certification and transition into a 'Cloud Security Compliance Specialist' role, you need to establish his development plan formally. Start by retrieving the job advertisement for the role he aims for. Reflecting on the 'Policy Writing' prerequisite, search and allocate the corresponding course. Follow this by updating his 'Policy Writing' skill proficiency to 'Intermediate'. Then, search for and connect him with an available mentor skilled in both 'Policy' and 'Leadership'. Lastly, initiate a new active goal with ID 'G303-3', type 'Certification', description 'Complete foundational policy course and achieve AWS Security Specialty certification.', last updated on '2025-11-12', and document this action in his team's training log with the following entry: 'David Adams assigned course and mentor for AWS Security certification path.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "David Adams"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Cloud Security Compliance Specialist"},
            ),
            Action(
                name="SearchCourses",
                kwargs={"skill": "Policy Writing"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U303", "course_id": "C1007"},
            ),
            Action(
                name="UpdateSkillProficiency",
                kwargs={
                    "user_id": "U303",
                    "skill": "Policy Writing",
                    "new_level": "Intermediate",
                },
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Policy", "Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U303", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U303"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T005",
                    "entry": "David Adams assigned course and mentor for AWS Security certification path.",
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
        instruction="Handle the review outcome of Alexander Adams's application for the 'Senior Data Scientist' position by hiring manager Ava Nguyen. While her application is not accepted for this current opening, Jack intends to prepare a development strategy for a potential future position. First, locate her application and modify its status to 'Rejected - Future Consideration'. Subsequently, assign her two courses based on the gaps in 'Machine Learning' and 'Python' skills noted in her application. Then, identify an available mentor specializing in 'Leadership' and connect them with her. Finally, initiate a new active objective with ID 'G310-2', specifying type as 'Role Transition', and outline the goal as 'Complete ML and Python training for future Data Scientist opportunities', with the most recent update on '2025-09-05'. Record this action in her team's training log with the note 'Alexander Adams placed on development track for future Data Scientist roles.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Alexander Adams"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U310", "job_id": "J001"},
            ),
            Action(
                name="UpdateApplicationStatus",
                kwargs={
                    "application_id": "APP002",
                    "status": "Rejected - Future Consideration",
                },
            ),
            Action(
                name="GetJobApplication",
                kwargs={"application_id": "APP002"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U310", "course_id": "C1001"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U310", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U310"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T008",
                    "entry": "Alexander Adams placed on development track for future Data Scientist roles.",
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
        instruction="Coordinate the advancement process for Harper Bennett due to hiring manager Ava Nguyen's positive impression of her application for the 'Senior Data Scientist' role. Initially, locate her application and set its status to 'Interview Scheduled'. Then, ensure she is shortlisted for the position. To proactively mitigate the 'Machine Learning' skill gap identified in her application, allocate the appropriate course following the policy guidelines. Moreover, find an available mentor with expertise in 'Leadership' and connect them with her. Lastly, insert an entry into her team's training log: 'Harper Bennett assigned ML course and mentor as part of interview process for Senior Data Scientist role.'",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="UpdateApplicationStatus",
                kwargs={"application_id": "APP001", "status": "Interview Scheduled"},
            ),
            Action(
                name="ShortlistCandidate",
                kwargs={"job_id": "J001", "candidate_id": "U302"},
            ),
            Action(
                name="GetJobApplication",
                kwargs={"application_id": "APP001"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_id": "U302"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T001",
                    "entry": "Harper Bennett assigned ML course and mentor as part of interview process for Senior Data Scientist role.",
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
        instruction="In order to ready Michael Rodriguez for spearheading the 'backend microservices redesign' project, ensure his development plan is formalized. Begin by locating his skill gap analysis specific to the 'Backend Tech Lead' role, identifying shortcomings in 'Systems Design', 'Team Leadership', and 'Kotlin'. Allocate the appropriate course for bridging the 'Team Leadership' gap. For technical skill gaps, seek out a mentor proficient in 'Engineering' and 'Career Growth' and connect them. Conclude by establishing a new active goal with ID 'G312-4', type 'Project', description 'Lead the backend microservices redesign by enhancing Systems Design and Kotlin skills.', with a last updated date of '2025-11-15', and log this action into his team's training record, noting: 'Michael Rodriguez assigned course and mentor for microservices redesign project.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Michael Rodriguez"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U312", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Engineering", "Career Growth"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U312", "mentor_id": "M101"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U312"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T003",
                    "entry": "Michael Rodriguez assigned course and mentor for microservices redesign project.",
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
        instruction="Michael Rodriguez is arranging his own development plan to achieve the 'DesignOps Lead' role. Initially, he intends to examine his complete course progress history. Post review, he plans to address his formal skill gap analysis for the role. Given the 'Stakeholder Alignment' gap, allocate the appropriate leadership course. Subsequently, find a mentor available with 'Leadership' proficiency and establish a link. Finally, set a new active goal with ID 'G304-4', type 'Skill Mastery', description 'Master Design Operations by formalizing two cross-team processes.', with a last updated date of '2025-11-18', and record this action in his team's training log, stating: 'Michael Rodriguez initiated development plan for DesignOps Lead role.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Michael Rodriguez"},
            ),
            Action(
                name="GetUserCourseProgress",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T002",
                    "entry": "Michael Rodriguez initiated development plan for DesignOps Lead role.",
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
        instruction="HR Partner Alexander Adams is tasked with handling the 'Succession Planning' workflow for candidate Michael Rodriguez. Initially, locate the workflow and change two stages: 'Candidate Identification' to 'Completed' and 'Skills Assessment' to 'In Progress'. Then, retrieve his skill gap analysis for the 'DesignOps Lead' role. Given his 'Stakeholder Alignment' gap, enroll him in the appropriate leadership course. After that, find a mentor with 'Leadership' expertise who is available and match them. Lastly, initiate a new active goal with ID 'G304-5', type 'Leadership', description 'Complete leadership course and lead stakeholder alignment for one cross-functional project.', with a last updated date of '2025-11-20', and record this activity in his team's training log with the following note: 'Michael Rodriguez assigned leadership course and mentor as part of succession plan.'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Michael Rodriguez"},
            ),
            Action(
                name="FindWorkflow",
                kwargs={"employee_id": "U304", "workflow_name": "Succession Planning"},
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Candidate Identification",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF002",
                    "stage": "Skills Assessment",
                    "status": "In Progress",
                },
            ),
            Action(
                name="GetSkillGap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U304", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
                name="GetUserProfile",
                kwargs={"user_id": "U304"},
            ),
            Action(
                name="UpdateTeamTrainingLog",
                kwargs={
                    "team_id": "T002",
                    "entry": "Michael Rodriguez assigned leadership course and mentor as part of succession plan.",
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
        instruction="Hiring manager Ava Nguyen has decided to not advance Harper Bennett's application for the 'Senior Data Scientist' role at this time, but intends to place her on a formal development track. First, identify her application and modify its status to 'Rejected - Future Consideration'. Then, access her 'Internal Promotion Process' workflow and amend two stages: 'Skills Assessment' to 'Completed' and 'Development Plan' to 'In Progress'. Subsequently, utilize the 'Machine Learning' gap from her application to assign the appropriate course. Finally, locate a mentor with 'Leadership' expertise who is available, connect them with her, and establish a new active goal with ID 'G302-5', type 'Role Transition', description 'Complete ML course and promotion workflow for future Data Scientist role.', with a last updated date of '2025-11-22'.",
        actions=[
            Action(
                name="FindUserByName",
                kwargs={"name": "Harper Bennett"},
            ),
            Action(
                name="FindJobByTitle",
                kwargs={"title": "Senior Data Scientist"},
            ),
            Action(
                name="FindApplication",
                kwargs={"user_id": "U302", "job_id": "J001"},
            ),
            Action(
                name="UpdateApplicationStatus",
                kwargs={
                    "application_id": "APP001",
                    "status": "Rejected - Future Consideration",
                },
            ),
            Action(
                name="FindWorkflow",
                kwargs={
                    "employee_id": "U302",
                    "workflow_name": "Internal Promotion Process",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Skills Assessment",
                    "status": "Completed",
                },
            ),
            Action(
                name="UpdateWorkflowStage",
                kwargs={
                    "workflow_id": "WF001",
                    "stage": "Development Plan",
                    "status": "In Progress",
                },
            ),
            Action(
                name="GetJobApplication",
                kwargs={"application_id": "APP001"},
            ),
            Action(
                name="AssignCourse",
                kwargs={"user_id": "U302", "course_id": "C1005"},
            ),
            Action(
                name="FindMentor",
                kwargs={"expertise": ["Leadership"]},
            ),
            Action(
                name="LinkMentor",
                kwargs={"user_id": "U302", "mentor_id": "M102"},
            ),
            Action(
                name="SetPerformanceGoal",
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
