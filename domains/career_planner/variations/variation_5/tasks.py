from domains.dto import Task, Action

TASKS = [
    # Task 1: Basic course enrollment with skill validation (Complexity: 8)
    Task(
        annotator="0",
        user_id="res_01",
        instruction="Ensure Jack Wang (U301) is registered for the Machine Learning course C1005 and update his promotion goal G301-1 to reflect the enrollment on 2025-10-02.",
        actions=[
            Action("getTodayDate", {}),
            Action(
                "getUserIdFromName", {"first_name": "Jack", "last_name": "Wang"}
            ),
            Action("searchUsers", {"filters": {"user_id": "U301"}}),
            Action(
                "enrollInCourse",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action("getGoal", {"user_id": "U301", "goal_id": "G301-1"}),
            Action(
                "updateGoal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {"last_updated": "2025-10-02"},
                },
            ),
            Action(
                "notifyHr",
                {"message": "U301 machine learning course enrollment completed"},
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "Goal G301-1 updated for user U301",
            '"notified": "HR"',
        ],
    ),
    # Task 2: Team assignment with basic mentorship setup (Complexity: 9)
    Task(
        annotator="pra-01",
        user_id="res_02",
        instruction="Place Ava Nguyen in the Analytics Team and set up a mentorship link with mentor M100, concentrating on analytics and career advancement. Next, inform him with this message: 'Welcome to the Analytics Team! You have been assigned a mentor to support your career growth.', and then inform HR with the following message: 'Ava Nguyen has been added to the Analytics Team and assigned mentor.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Harper", "last_name": "King"},
            ),
            Action("addTeamMember", {"team_id": "T001", "user_id": "U305"}),
            Action("computeMentorLoad", {"mentor_id": "M100"}),
            Action("getTodayDate", {}),
            Action(
                "addMentorshipRelationship",
                {
                    "mentor_id": "M100",
                    "mentee_id": "U305",
                    "status": "Active",
                    "start_date": "2025-10-02",
                    "focus_areas": ["Analytics", "Career Growth"],
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U305",
                    "message": "Welcome to the Analytics Team! You have been assigned a mentor to support your career growth.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Ava Nguyen has been added to the Analytics Team and assigned mentor."
                },
            ),
        ],
        outputs=[
            "User U305 added to team T001",
            "Mentorship relationship MR011 created",
            "notified_user",
            "notified",
        ],
    ),
    # Task 3: Skills assessment with course recommendation (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_03",
        instruction="Assign Alexander Adams to a foundational UX course to boost her skills and update her development goal with 'Active - Course Assigned'. Afterwards, send her a notification with the message: 'You have been enrolled in the 'UX Design Fundamentals' course to support your development goals.', and then inform hr with the message: 'Alexander Adams has been enrolled in course UX Design Fundamentals'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U307", "course_id": "C1002", "enroll_date": "2025-10-02"},
            ),
            Action("listUserGoals", {"user_id": "U307"}),
            Action(
                "updateGoal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "status": "Active - Course Assigned",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("getCourse", {"course_id": "C1002"}),
            Action(
                "notifyUser",
                {
                    "user_id": "U307",
                    "message": "You have been enrolled in the 'UX Design Fundamentals' course to support your development goals.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Alexander Adams has been enrolled in course UX Design Fundamentals."
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1002",
            "Goal G307-1 updated for user U307",
            "notified_user",
            "notified",
        ],
    ),
    # Task 4: Mentorship session scheduling with capacity check (Complexity: 8)
    Task(
        annotator="0",
        user_id="res_04",
        instruction="Set up the next mentorship session for David Adams (U304) two weeks from today on 2025-10-16. Inform him with the message: 'Your next mentorship session has been scheduled. Please check your calendar for details.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action("listUserMentorships", {"user_id": "U304"}),
            Action("getTodayDate", {}),
            Action("listUserGoals", {"user_id": "U304"}),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR002", "session_date": "2025-10-16"},
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR002",
                    "updates": {"next_session_date": "2025-10-16"},
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "Your next mentorship session has been scheduled. Please check your calendar for details.",
                },
            ),
        ],
        outputs=[
            '"scheduled_for": "2025-10-16"',
            "relationship MR002 updated",
            "notified_user",
        ],
    ),
    # Task 5: Certification tracking with goal alignment (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_05",
        instruction="Handle the registration of the 'AWS Security Specialty' certification from 'AWS' for David Adams, assigning a new certification ID 'C7011' and set up the exam for 60 days from today. Modify his certification goal to denote a 10% advancement. Inform HR through the message: 'David Adams (U303) has registered for the AWS Security Specialty exam.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("searchUsers", {"filters": {"user_id": "U303"}}),
            Action("getTodayDate", {}),
            Action(
                "addUserCertification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7011",
                        "cert_name": "AWS Security Specialty",
                        "issuer": "AWS",
                        "issue_date": None,
                        "scheduled_exam_date": "2025-12-01",
                    },
                },
            ),
            Action("listUserGoals", {"user_id": "U303"}),
            Action(
                "updateGoal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 10,
                        "status": "In Progress - Exam Scheduled",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "David Adams (U303) has registered for the AWS Security Specialty exam."
                },
            ),
        ],
        outputs=[
            "Certification AWS Security Specialty added for user U303",
            "Goal G303-1 updated for user U303",
            '"notified": "HR"',
        ],
    ),
    # Task 6: Course progress update with goal synchronization (Complexity: 9)
    Task(
        annotator="0",
        user_id="res_06",
        instruction="Update Harper Bennett's 'Python' course progress to 50%. Additionally, adjust the 'last_updated' field concerning her career goal related to 'Python'. Finally, send a notification to her with the message: 'Your progress on the Python course has been updated to 50%. Keep up the great work!' and alert HR with the message: 'Harper Bennett has reached a 50% progress milestone in her Python course, supporting her development goal.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("getCourseIdByName", {"course_name": "Python"}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("getTodayDate", {}),
            Action(
                "updateUserCourseProgress",
                {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "updates": {
                        "current_progress_percent": 50,
                    },
                },
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"last_updated": "2025-10-02"},
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "Your progress on the Python course has been updated to 50%. Keep up the great work!",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Harper Bennett has reached a 50% progress milestone in her Python course, supporting her development goal."
                },
            ),
        ],
        outputs=[
            "course progress updated",
            "Goal G302-1 updated for user U302",
            "notified_user",
            "notified",
        ],
    ),
    # Task 7: Workflow stage advancement with validation (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_07",
        instruction="Progress Harper Bennett's promotion workflow to the 'Development Plan' phase. Determine who the designated planner is for this stage, find out their full name, and update the workflow notes to indicate their assignment. Enroll Ava in the course recommended by the workflow. Additionally, update her career goal related to 'Python' by including: 'Development plan now active under WF001.' in the description. Notify Ava with the message: 'Your promotion workflow has progressed to the Development Plan stage and you have been enrolled in required training.' and inform the assigned planner with the message: 'You have been designated as the planner for Harper Bennett's development plan in promotion workflow WF001.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("findHrWorkflowForUser", {"user_id": "U302"}),
            Action("getHrWorkflow", {"workflow_id": "WF001"}),
            Action("searchUsers", {"filters": {"user_id": "U310"}}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("getGoal", {"user_id": "U302", "goal_id": "G302-1"}),
            Action("getTodayDate", {}),
            Action(
                "updateHrWorkflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "notes_append": "Plan assigned to planner Alexander Adams.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "goal_description": "Add Python to clinical-analytics toolkit and deliver an internal POC to demonstrate leadership in data-driven decision making. Development plan now active under WF001.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "Your promotion workflow has advanced to the Development Plan stage and you have been enrolled in required training.",
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U310",
                    "message": "You have been assigned as the planner for Harper Bennett's development plan in promotion workflow WF001.",
                },
            ),
        ],
        outputs=[
            "workflow WF001 updated",
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            "notified_user",
            "notified_user",
        ],
    ),
    # Task 8: Dual competency development with mentorship enhancement (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_08",
        instruction="Initially, confirm that Robert Thompson satisfies the '3+ years PM experience' requirement for the 'Project Management Professional (PMP)' course. If he does, proceed to enroll him. Then, update his goal related to 'Staff SRE' by appending the note: 'PMP course enrolled to support leadership path.' Moreover, update his mentorship relationship by adding 'Strategic Leadership' to the current focus areas. Finally, notify both Alexander and his manager about the enrollment using the message: 'Robert Thompson has been enrolled in the PMP course to support his strategic development goals.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("searchUsers", {"filters": {"user_id": "U306"}}),
            Action(
                "getCourseIdByName",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action("getCourse", {"course_id": "C1004"}),
            Action("listUserGoals", {"user_id": "U306"}),
            Action("listUserMentorships", {"user_id": "U306"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U306", "course_id": "C1004", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "goal_description": "Advance to Staff Site Reliability Engineer and lead reliability roadmap. PMP course enrolled to support leadership path.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR004",
                    "updates": {
                        "focus_areas": [
                            "Site Reliability Engineering",
                            "Leadership",
                            "Infrastructure",
                            "Strategic Leadership",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U306",
                    "message": "Robert Thompson has been enrolled in the PMP course to support his strategic development goals.",
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U312",
                    "message": "Robert Thompson has been enrolled in the PMP course to support his strategic development goals.",
                },
            ),
        ],
        outputs=[
            "User U306 enrolled in course C1004",
            "Goal G306-1 updated for user U306",
            "relationship MR004 updated",
            "notified_user",
            "notified_user",
        ],
    ),
    # Task 9: Data visualization competency with specialized training (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_09",
        instruction="Facilitate David Adams's growth by enrolling him in the 'Data Visualization with Tableau' course. Modify his primary goal metric associated with 'AWS Security' to include 'Pass AWS Security Specialty exam and complete Tableau course'. Additionally, revise his mentorship details by incorporating 'Data Visualization' into the focus areas. Inform him with the message: 'You have been enrolled in a Tableau course as a foundational step towards your AWS Security goal, which has been updated to reflect this.' and alert HR with the message: 'David Adams has been enrolled in supplemental Tableau training to support his primary AWS Security goal.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("getGoal", {"user_id": "U303", "goal_id": "G303-1"}),
            Action("listUserMentorships", {"user_id": "U303"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U303", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "metric": "Pass AWS Security Specialty exam and complete Tableau course",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Career Transition",
                            "Data Visualization",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U303",
                    "message": "You have been enrolled in a Tableau course as a foundational step towards your AWS Security goal, which has been updated to reflect this.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "David Adams has been enrolled in supplemental Tableau training to support his primary AWS Security goal."
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1003",
            "Goal G303-1 updated for user U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 10: Cross-functional team integration with accessibility focus (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_10",
        instruction="Place Alexander Adams on the 'Product Design Team'. Augment her primary career goal by adding the note: 'Now a member of the Product Design Team to lead accessibility initiatives.' Arrange a mentorship session for the following week. Inform Chloe with the message: 'You have been assigned to the Product Design Team to lead accessibility initiatives. Your career goal has been updated and a mentorship session is scheduled.' Also, notify her new manager and HR with the message: 'Alexander Adams has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("getTeamIdByName", {"team_name": "Product Design Team"}),
            Action("getTeam", {"team_id": "T002"}),
            Action("listUserGoals", {"user_id": "U307"}),
            Action("listUserMentorships", {"user_id": "U307"}),
            Action("getTodayDate", {}),
            Action("addTeamMember", {"team_id": "T002", "user_id": "U307"}),
            Action(
                "updateGoal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "goal_description": "Publish company-wide accessibility guidelines and train designers. Now a member of the Product Design Team to lead accessibility initiatives.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR003", "session_date": "2025-10-09"},
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U307",
                    "message": "You have been assigned to the Product Design Team to lead accessibility initiatives. Your career goal has been updated and a mentorship session is scheduled.",
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "Alexander Adams has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Alexander Adams has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated."
                },
            ),
        ],
        outputs=[
            "User U307 added to team T002",
            "Goal G307-1 updated for user U307",
            '"scheduled_for": "2025-10-09"',
            "notified_user",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 11: ML specialization with backup mentorship (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_11",
        instruction="Facilitate Ava Nguyen's development by enrolling him in the 'Machine Learning Specialization' course. Revise his goal concerning 'Director of Data Science' to incorporate this enrollment by adding 'and complete ML Specialization' to its metric. Additionally, augment his mentorship relationship by including 'Machine Learning' in the current focus areas. Inform him with the message: 'You have been enrolled in the ML Specialization as a step towards your Director goal, which has been updated to reflect this.' and inform HR with the message: 'Ava Nguyen has been enrolled in supplemental ML training to support his primary promotion goal.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("getGoal", {"user_id": "U301", "goal_id": "G301-1"}),
            Action("listUserMentorships", {"user_id": "U301"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "metric": "Complete ML course and publish 2 predictive models and complete ML Specialization",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Machine Learning",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U301",
                    "message": "You have been enrolled in the ML Specialization as a step towards your Director goal, which has been updated to reflect this.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Ava Nguyen has been enrolled in supplemental ML training to support his primary promotion goal."
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "Goal G301-1 updated for user U301",
            "relationship MR001 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 12: Performance intervention with comprehensive support (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_12",
        instruction="Facilitate Michael Rodriguez' performance enhancement by enrolling him in the 'UX Design Fundamentals' course. Establish a new 'Skill Development' goal for him with ID 'G304-2' and description 'Complete UX Design Fundamentals to strengthen technical foundations'. Strengthen his mentorship relationship by adding 'Technical Foundation Support' to the focus areas. Inform him with the message: 'A performance support plan has been initiated. You have been enrolled in a foundational course and a new goal has been set. Please connect with your mentor.' and inform HR with the message: 'A performance support plan has been activated for Michael Rodriguez, including course enrollment and a new development goal.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action("getCourseIdByName", {"course_name": "UX Design Fundamentals"}),
            Action("listUserMentorships", {"user_id": "U304"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U304", "course_id": "C1002", "enroll_date": "2025-10-02"},
            ),
            Action(
                "addGoal",
                {
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-2",
                        "goal_type": "Skill Development",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": "Technical Foundation Support",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "A performance support plan has been initiated. You have been enrolled in a foundational course and a new goal has been set. Please connect with your mentor.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A performance support plan has been activated for Michael Rodriguez, including course enrollment and a new development goal."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1002",
            "goal G304-2 added for U304",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 13: Comprehensive progress analysis with targeted interventions (Complexity: 15)
    Task(
        annotator="0",
        user_id="res_13",
        instruction="To bridge skill gaps, register Harper Bennett for the 'Machine Learning Specialization' course. Modify her goal associated with 'Python' to incorporate this new training. Additionally, create a new mentorship link for her by choosing the first available mentor (starting alphabetically from M100) concentrating on 'Machine Learning'. Inform her with the message: 'To support your career advancement, you have been enrolled in the Machine Learning Specialization course and assigned a new mentor.' and inform HR with the message: 'Harper Bennett has been enrolled in targeted ML training and assigned a mentor to address identified skill gaps.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("getCourseIdByName", {"course_name": "Machine Learning"}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("computeMentorLoad", {"mentor_id": "M100"}),
            Action(
                "addMentorshipRelationship",
                {
                    "mentor_id": "M100",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Machine Learning"],
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "To support your career advancement, you have been enrolled in the Machine Learning Specialization course and assigned a new mentor.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Harper Bennett has been enrolled in targeted ML training and assigned a mentor to address identified skill gaps."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 14: Technical competency advancement with certification alignment (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_14",
        instruction="In order to enhance David Adams's technical skills, register him for the 'Advanced Python' course. Change his goal concerning 'AWS Security' by setting its completion date to 90 days from now. Moreover, revise his mentorship engagement to set the focus areas to Cloud Security, Compliance, and Python Development. Inform him with the message: 'To support your technical development, you have been enrolled in the Advanced Python course. Your AWS certification goal and mentorship plan have been updated accordingly.' and inform HR with the message: 'David Adams has been enrolled in Python training to complement his cloud security goals. His development plan has been updated.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("getCourseIdByName", {"course_name": "Advanced Python"}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("listUserMentorships", {"user_id": "U303"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U303", "course_id": "C1001", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "target_date": "2025-12-31",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Python Development",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U303",
                    "message": "To support your technical development, you have been enrolled in the Advanced Python course. Your AWS certification goal and mentorship plan have been updated accordingly.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "David Adams has been enrolled in Python training to complement his cloud security goals. His development plan has been updated."
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1001",
            "Goal G303-1 updated for user U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 15: AWS certification pathway with readiness assessment (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_15",
        instruction="In order to prepare Michael Rodriguez for certification, modify his primary career objective related to 'DesignOps' by adding the note: 'This goal is supported by pursuing AWS Solutions Architect certification.' Register him for the 'AWS Solutions Architect Associate' exam (cert ID 'C7012') happening in 180 days. Additionally, adjust his mentorship focus areas to encompass 'AWS Certification Prep'. Inform him with the message: 'A new development path has been created for you to pursue AWS certification. Your primary career goal and mentorship plan have been updated.' and inform HR with the message: 'A certification path for AWS Solutions Architect Associate has been established for Michael Rodriguez.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U304", "keyword": "DesignOps"},
            ),
            Action("listUserMentorships", {"user_id": "U304"}),
            Action("getTodayDate", {}),
            Action(
                "addUserCertification",
                {
                    "user_id": "U304",
                    "cert": {
                        "cert_id": "C7012",
                        "cert_name": "AWS Solutions Architect Associate",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2026-03-31",
                    },
                },
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U304",
                    "goal_id": "G304-1",
                    "updates": {
                        "goal_description": "Move into DesignOps Lead role and formalize cross-team processes. This goal is supported by pursuing AWS Solutions Architect certification.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "AWS Certification Prep",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "A new development path has been created for you to pursue AWS certification. Your primary career goal and mentorship plan have been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A certification path for AWS Solutions Architect Associate has been established for Michael Rodriguez."
                },
            ),
        ],
        outputs=[
            "Certification AWS Solutions Architect Associate added for user U304",
            "Goal G304-1 updated for user U304",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 16: Mentor capacity optimization with reassignment (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_16",
        instruction="To improve mentor capacity, transfer Alexander Adams to a different mentor. The replacement mentor must be the one with the fewest current mentees (checking M101, M102, and M103), with alphabetical order used as a tiebreaker. The new relationship should maintain the focus areas from the previous one. The prior relationship should be labeled as 'Inactive - Reassigned'. Notify Chloe with the message: 'To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.' and inform HR with the message: 'Mentor load balancing has been performed. Alexander Adams has been reassigned to a new mentor.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("listUserMentorships", {"user_id": "U307"}),
            Action("getTodayDate", {}),
            Action("computeMentorLoad", {"mentor_id": "M101"}),
            Action("computeMentorLoad", {"mentor_id": "M102"}),
            Action("computeMentorLoad", {"mentor_id": "M103"}),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "status": "Inactive - Reassigned",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "addMentorshipRelationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Accessibility",
                        "Mentorship",
                        "Design Leadership",
                    ],
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U307",
                    "message": "To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Mentor load balancing has been performed. Alexander Adams has been reassigned to a new mentor."
                },
            ),
        ],
        outputs=[
            "relationship MR003 updated",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 17: Data visualization mastery with specialized mentorship (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_17",
        instruction="To verify Harper Bennett's capability in data visualization, sign her up for the 'Data Visualization with Tableau' course. Initiate a new 'Skill Development' goal for her using ID 'G302-2' and include the description 'Achieve proficiency in Tableau for clinical analytics'. Also, set up a new mentorship for her with the available mentor found by checking M100-M103, prioritized by the lowest workload, then alphabetically, focusing on Clinical Analytics, Python, and Tableau. Inform her with the message: 'A new development path has been created for you to master data visualization. You have been enrolled in a Tableau course, and a new goal and mentorship have been established.' and alert HR with the message: 'Harper Bennett has been enrolled in Tableau training with a new goal and mentorship to support her data visualization competency.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "addGoal",
                {
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-2",
                        "goal_type": "Skill Development",
                        "goal_description": "Achieve proficiency in Tableau for clinical analytics",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("computeMentorLoad", {"mentor_id": "M100"}),
            Action("computeMentorLoad", {"mentor_id": "M101"}),
            Action("computeMentorLoad", {"mentor_id": "M102"}),
            Action("computeMentorLoad", {"mentor_id": "M103"}),
            Action(
                "addMentorshipRelationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Clinical Analytics", "Python", "Tableau"],
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "A new development path has been created for you to master data visualization. You have been enrolled in a Tableau course, and a new goal and mentorship have been established.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Harper Bennett has been enrolled in Tableau training with a new goal and mentorship to support her data visualization competency."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1003",
            "goal G302-2 added for U302",
            "Mentorship relationship MR014 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 18: Goal progress validation with technical advancement (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_18",
        instruction="To confirm the progress of David Adams's AWS Security goal, register him in the 'Advanced Python' course. Adjust his 'AWS Security' goal progress to reflect 25%. Arrange for a mentorship session to occur 14 days from today. Inform him with the message: 'Your AWS Security goal progress has been updated. You have been enrolled in a new course and a mentorship session has been scheduled to discuss your technical advancement.' and alert HR with the message: 'David Adams's AWS Security goal has been updated with a new course enrollment and a scheduled mentorship session.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("getCourseIdByName", {"course_name": "Advanced Python"}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("listUserMentorships", {"user_id": "U303"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U303", "course_id": "C1001", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 25,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR006", "session_date": "2025-10-16"},
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U303",
                    "message": "Your AWS Security goal progress has been updated. You have been enrolled in a new course and a mentorship session has been scheduled to discuss your technical advancement.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "David Adams's AWS Security goal has been updated with a new course enrollment and a scheduled mentorship session."
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1001",
            "Goal G303-1 updated for user U303",
            '"scheduled_for": "2025-10-16"',
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 19: Cross-functional competency with team integration (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_19",
        instruction="Handle Michael Rodriguez' preparation for cross-functional leadership by enrolling him in the 'Machine Learning Specialization' program. Introduce a new 'Leadership' goal with the ID 'G304-2', described as 'Lead a cross-functional design project leveraging ML insights'. Update his mentorship focus areas to ['Design Operations', 'Leadership', 'Process Management', 'Cross-functional Collaboration']. Inform him with the message: 'To support your growth into cross-functional leadership, you have been enrolled in a Machine Learning course and a new leadership goal has been created.' and inform HR with the message: 'Michael Rodriguez has been enrolled in ML training to support a new cross-functional leadership goal.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action("listUserMentorships", {"user_id": "U304"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U304", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "addGoal",
                {
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-2",
                        "goal_type": "Leadership",
                        "goal_description": "Lead a cross-functional design project leveraging ML insights",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Cross-functional Collaboration",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "To support your growth into cross-functional leadership, you have been enrolled in a Machine Learning course and a new leadership goal has been created.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Michael Rodriguez has been enrolled in ML training to support a new cross-functional leadership goal."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1005",
            "goal G304-2 added for U304",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 20: Strategic development with Agile competency (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_20",
        instruction="Coordinate the creation of a strategic development plan for Michael Rodriguez by enrolling him in the 'Agile Product Management' course. Update his mentorship focus areas by adding 'Agile Methodologies'. Arrange a mentorship session to occur 14 days from today. Inform him with the message: 'A new strategic development plan has been initiated. You have been enrolled in an Agile course, and a mentorship session has been scheduled to discuss next steps.' and inform HR with the message: 'A strategic development plan has been established for Michael Rodriguez, including Agile course enrollment and mentorship alignment.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Agile Product Management"},
            ),
            Action("listUserMentorships", {"user_id": "U304"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U304", "course_id": "C1006", "enroll_date": "2025-10-02"},
            ),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR002", "session_date": "2025-10-16"},
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Agile Methodologies",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "A new strategic development plan has been initiated. You have been enrolled in an Agile course, and a mentorship session has been scheduled to discuss next steps.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A strategic development plan has been established for Michael Rodriguez, including Agile course enrollment and mentorship alignment."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1006",
            '"scheduled_for": "2025-10-16"',
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 21: ML competency validation with workflow coordination (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_21",
        instruction="Ensure Ava Nguyen's ML skills by registering him for the 'Machine Learning Specialization' course. Adjust his goal concerning the Director of Data Science to a 45% completion rate. Additionally, modify his mentorship relationship to highlight Leadership, Data Science, Career Growth, and Machine Learning as focus areas. Inform HR with the message: 'Ava Nguyen has been enrolled in the Machine Learning Specialization to validate competency for his promotion goal. His development plan has been updated.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("listUserMentorships", {"user_id": "U301"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U301", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Machine Learning",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Ava Nguyen has been enrolled in the Machine Learning Specialization to validate competency for his promotion goal. His development plan has been updated."
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "Goal G301-1 updated for user U301",
            "relationship MR001 updated",
            '"notified": "HR"',
        ],
    ),
    # Task 22: Development Plan coordination with dual course assignment (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_22",
        instruction="Create a development plan for Harper Bennett by moving her promotion workflow to the 'Development Plan' phase and scheduling a review date 60 days from now. Enroll her in the 'Machine Learning Specialization' and 'Data Visualization with Tableau' courses. Modify her goal associated with 'Python' to show 40% progress. Communicate to her with the message: 'Your development plan has been established. You have been enrolled in new courses to support your promotion goals.' and notify HR with the message: 'A development plan for Harper Bennett has been established, including new course enrollments and a scheduled review date.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("findHrWorkflowForUser", {"user_id": "U302"}),
            Action(
                "getCourseIdByName",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("getTodayDate", {}),
            Action(
                "updateHrWorkflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "review_date": "2025-12-01",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 40,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "Your development plan has been established. You have been enrolled in new courses to support your promotion goals.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A development plan for Harper Bennett has been established, including new course enrollments and a scheduled review date."
                },
            ),
        ],
        outputs=[
            "workflow WF001 updated",
            "User U302 enrolled in course C1005",
            "User U302 enrolled in course C1003",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 23: Leadership advancement with mentorship enhancement (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_23",
        instruction="In order to groom Alexander Adams for a leadership position, register her in the 'Agile Product Management' course. Amend her primary goal relating to accessibility to add the note: 'and master Agile methodologies for future leadership roles.' Additionally, modify her mentorship focus areas to encompass 'Agile Leadership'. Inform Chloe, her manager, and HR with the message: 'A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("searchUsers", {"filters": {"user_id": "U307"}}),
            Action(
                "getCourseIdByName",
                {"course_name": "Agile Product Management"},
            ),
            Action("listUserGoals", {"user_id": "U307"}),
            Action("listUserMentorships", {"user_id": "U307"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U307", "course_id": "C1006", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "goal_description": "Publish company-wide accessibility guidelines and train designers. and master Agile methodologies for future leadership roles.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "focus_areas": [
                            "Accessibility",
                            "Mentorship",
                            "Design Leadership",
                            "Agile Leadership",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U307",
                    "message": "A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this.",
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this."
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1006",
            "Goal G307-1 updated for user U307",
            "relationship MR003 updated",
            "notified_user",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 24: Post-MBA strategic positioning with certification planning (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_24",
        instruction="To carve out a post-MBA strategic leadership route for David Adams, sign him up for the 'Project Management Professional (PMP)' certification (cert ID 'C7014') with an exam scheduled 225 days from today. Enlist him in the 'Agile Product Management' course. Establish a new 'Leadership' goal with ID 'G303-2' and description 'Achieve PMP certification and demonstrate strategic leadership'. Revise his mentorship focus areas to include 'Strategic Leadership'. Communicate to him with the message: 'Your post-MBA leadership pathway has been established. You have been registered for the PMP exam, enrolled in a new course, and a new goal has been created.' and inform HR with the message: 'A post-MBA strategic leadership pathway has been established for David Adams, including PMP registration and a new development goal.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Agile Product Management"},
            ),
            Action("listUserMentorships", {"user_id": "U303"}),
            Action("getTodayDate", {}),
            Action(
                "addUserCertification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7014",
                        "cert_name": "Project Management Professional (PMP)",
                        "issuer": "PMI",
                        "scheduled_exam_date": "2026-05-14",
                    },
                },
            ),
            Action(
                "enrollInCourse",
                {"user_id": "U303", "course_id": "C1006", "enroll_date": "2025-10-02"},
            ),
            Action(
                "addGoal",
                {
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Leadership",
                        "goal_description": "Achieve PMP certification and demonstrate strategic leadership",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Strategic Leadership",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U303",
                    "message": "Your post-MBA leadership pathway has been established. You have been registered for the PMP exam, enrolled in a new course, and a new goal has been created.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A post-MBA strategic leadership pathway has been established for David Adams, including PMP registration and a new development goal."
                },
            ),
        ],
        outputs=[
            "Certification Project Management Professional (PMP) added for user U303",
            "User U303 enrolled in course C1006",
            "goal G303-2 added for U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 25: Stakeholder management competency with mentor coordination (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_25",
        instruction="Handle the enhancement of Michael Rodriguez' stakeholder management skills by enrolling him in the 'Project Management Professional (PMP)' course. Amend his mentorship focus areas to encompass 'Stakeholder Alignment'. Inform him with the message: 'To advance your stakeholder management competency, you have been enrolled in a leadership course and your mentorship plan has been updated.' and alert HR with the message: 'Michael Rodriguez has been enrolled in leadership training to support his stakeholder management competency.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Project Management Professional (PMP)"},
            ),
            Action("listUserMentorships", {"user_id": "U304"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U304", "course_id": "C1004", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Stakeholder Alignment",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U304",
                    "message": "To advance your stakeholder management competency, you have been enrolled in a leadership course and your mentorship plan has been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Michael Rodriguez has been enrolled in leadership training to support his stakeholder management competency."
                },
            ),
        ],
        outputs=[
            "User U304 enrolled in course C1004",
            "relationship MR002 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 26: Foundation skills acceleration with goal synchronization (Complexity: 9)
    Task(
        annotator="0",
        user_id="res_26",
        instruction="Coordinate the acceleration of Harper Bennett's foundation skills by enrolling her in the 'Advanced Python' course. Update her progress related to 'Python' by adjusting it to 10%. Inform her with the message: 'To accelerate your foundation skills, you have been enrolled in the Advanced Python course and your goal progress has been updated.' and notify HR with the message: 'Harper Bennett has been enrolled in Python training to accelerate her foundation skills. Her goal progress has been synchronized.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("getCourseIdByName", {"course_name": "Advanced Python"}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1001", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 10,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "To accelerate your foundation skills, you have been enrolled in the Advanced Python course and your goal progress has been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Harper Bennett has been enrolled in Python training to accelerate her foundation skills. Her goal progress has been synchronized."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1001",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 27: Mentor capacity monitoring with alert generation (Complexity: 7)
    Task(
        annotator="0",
        user_id="res_27",
        instruction="To enhance mentor capacity for Mentor M100, reassign their latest mentee, Alexander Adams, to a different mentor. Choose the new mentor with the lowest current mentee count from M101, M102, and M103, using an alphabetical order if needed to decide ties. Ensure the new relationship retains the focus areas of the previous one. Label the previous relationship as 'Inactive - Reassigned'. Inform Chloe with the message: 'To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.' and notify HR with the message: 'Mentor load balancing has been performed. Alexander Adams has been reassigned from Mentor M100 to a new mentor to optimize capacity.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("listUserMentorships", {"user_id": "U307"}),
            Action("getTodayDate", {}),
            Action("computeMentorLoad", {"mentor_id": "M101"}),
            Action("computeMentorLoad", {"mentor_id": "M102"}),
            Action("computeMentorLoad", {"mentor_id": "M103"}),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "status": "Inactive - Reassigned",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "addMentorshipRelationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Accessibility", "Mentorship", "Design Leadership"],
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U307",
                    "message": "To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Mentor load balancing has been performed. Alexander Adams has been reassigned from Mentor M100 to a new mentor to optimize capacity."
                },
            ),
        ],
        outputs=[
            "relationship MR003 updated",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 28: Skill gap remediation with ML specialization (Complexity: 10)
    Task(
        annotator="0",
        user_id="res_28",
        instruction="To fill Harper Bennett's skill gaps, register her in the 'Machine Learning Specialization' course. Align her 'Python' goal by updating its progress to 15%. Inform her with the message: 'To address your skill gaps, you have been enrolled in the Machine Learning Specialization and your goal progress has been updated.' and notify HR with the message: 'Harper Bennett has been enrolled in ML training to address identified skill gaps. Her goal progress has been synchronized.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Machine Learning Specialization"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 15,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "To address your skill gaps, you have been enrolled in the Machine Learning Specialization and your goal progress has been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Harper Bennett has been enrolled in ML training to address identified skill gaps. Her goal progress has been synchronized."
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 29: Transition goal management with market alignment (Complexity: 8)
    Task(
        annotator="0",
        user_id="res_29",
        instruction="Handle the synchronization of Ava Nguyen's 'Director of Data Science' goal by aligning its progress with his current average course completion rate. Should the updated progress exceed 50%, arrange a review meeting with his mentor for the following week. Inform Jack of the goal update, and should a session be arranged, include this detail in his notification and also inform his mentor.",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("computeAverageProgress", {"user_id": "U301"}),
            Action("listUserMentorships", {"user_id": "U301"}),
            Action("getTodayDate", {}),
            Action(
                "updateGoal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 72.5,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR001", "session_date": "2025-10-09"},
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U301",
                    "message": "Your Director promotion goal has been updated to 72.5% based on your average course progress. A review session with your mentor has been scheduled for 2025-10-09.",
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "M102",
                    "message": "A progress review session with your mentee, Ava Nguyen, has been scheduled for 2025-10-09 to discuss his recent goal advancement.",
                },
            ),
        ],
        outputs=[
            "Goal G301-1 updated for user U301",
            '"scheduled_for": "2025-10-09"',
            "notified_user",
            "notified_user",
        ],
    ),
    # Task 30: Analytics mastery enhancement with supplemental training (Complexity: 9)
    Task(
        annotator="0",
        user_id="res_30",
        instruction="Coordinate Ava Nguyen's advancement in analytics by registering him for the 'Data Visualization with Tableau' course. Keep track of this by adjusting his 'Director of Data Science' goal progress to 50%. Notify him with the message: 'To enhance your analytics mastery, you have been enrolled in a Tableau course and your goal progress has been updated.' and inform HR with the message: 'Ava Nguyen has been enrolled in supplemental Tableau training to support his analytics mastery. His goal progress has been updated.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                "getCourseIdByName",
                {"course_name": "Data Visualization with Tableau"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U301", "course_id": "C1003", "enroll_date": "2025-10-02"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U301",
                    "message": "To enhance your analytics mastery, you have been enrolled in a Tableau course and your goal progress has been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Ava Nguyen has been enrolled in supplemental Tableau training to support his analytics mastery. His goal progress has been updated."
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1003",
            "Goal G301-1 updated for user U301",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 31: Workflow progression with skill validation (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_31",
        instruction="Ensure Harper Bennett's promotion workflow is advanced to Development Plan with verification of Skills Assessment completion and initiation of ML course enrollment.",
        actions=[
            Action(
                "getUserIdFromName", {"first_name": "Ava", "last_name": "Nguyen"}
            ),
            Action("searchUsers", {"filters": {"user_id": "U302"}}),
            Action("getTodayDate", {}),
            Action("getHrWorkflow", {"workflow_id": "WF001"}),
            Action(
                "updateHrWorkflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "skills_assessment_completed": "2025-10-02",
                    },
                },
            ),
            Action(
                "enrollInCourse",
                {"user_id": "U302", "course_id": "C1005", "enroll_date": "2025-10-02"},
            ),
            Action("getGoal", {"user_id": "U302", "goal_id": "G302-1"}),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {"last_updated": "2025-10-02"},
                },
            ),
            Action(
                "notifyHr",
                {"message": "WF001 progression to Development Plan completed"},
            ),
        ],
        outputs=[
            "workflow WF001 updated",
            "User U302 enrolled in course C1005",
            "Goal G302-1 updated for user U302",
            '"notified": "HR"',
        ],
    ),
    # Task 32: Leadership coaching optimization with milestone achievement (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_32",
        instruction="In order to complete Robert Thompson' leadership development, confirm that his primary goal associated with 'Staff SRE' is recorded as 100% finished, and add the note 'Final leadership milestone achieved.' to its description. Arrange a concluding coaching session with his mentor for the coming week. Inform Alexander, his mentor, and HR by sending the message: 'Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("listUserGoals", {"user_id": "U306"}),
            Action("listUserMentorships", {"user_id": "U306"}),
            Action("getTodayDate", {}),
            Action(
                "updateGoal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 100,
                        "status": "Completed",
                        "goal_description": "Advance to Staff Site Reliability Engineer and lead reliability roadmap. Final leadership milestone achieved.",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR004", "session_date": "2025-10-09"},
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U306",
                    "message": "Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan.",
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "M101",
                    "message": "Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan."
                },
            ),
        ],
        outputs=[
            "Goal G306-1 updated for user U306",
            '"scheduled_for": "2025-10-09"',
            "notified_user",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 33: Performance review with goal advancement (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_33",
        instruction="Upon the completion of his quarterly performance review, adjust Ava Nguyen's goal for the 'Director of Data Science' by updating its progress to 65%. Inform him with the message: 'Your quarterly performance review has been completed and your promotion goal progress has been updated.' and alert HR with the message: 'The quarterly performance review for Ava Nguyen is complete. His promotion goal has been updated accordingly.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Jack", "last_name": "Wang"},
            ),
            Action("searchUsers", {"filters": {"user_id": "U301"}}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U301", "keyword": "Director of Data Science"},
            ),
            Action("getTodayDate", {}),
            Action(
                "updateGoal",
                {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 65,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U301",
                    "message": "Your quarterly performance review has been completed and your promotion goal progress has been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "The quarterly performance review for Ava Nguyen is complete. His promotion goal has been updated accordingly."
                },
            ),
        ],
        outputs=[
            "Goal G301-1 updated for user U301",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 34: Accelerated learning with workflow advancement (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_34",
        instruction="Conduct an accelerated learning program initiation for Harper Bennett by adjusting her 'Advanced Python' course progress to 25%. Move her promotion workflow to the 'Training Assignment' phase. Modify her goal related to 'Python' to reflect 45% progress. Inform her with the message: 'Your accelerated learning program has been initiated. Your course and goal progress have been updated, and your promotion workflow has been advanced.' and alert HR with the message: 'An accelerated learning program for Harper Bennett has been initiated. Her promotion workflow has advanced to the Training Assignment stage.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action("getCourseIdByName", {"course_name": "Advanced Python"}),
            Action("findHrWorkflowForUser", {"user_id": "U302"}),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U302", "keyword": "Python"},
            ),
            Action("getTodayDate", {}),
            Action(
                "updateUserCourseProgress",
                {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "updates": {
                        "current_progress_percent": 25,
                        "status": "In Progress",
                    },
                },
            ),
            Action(
                "updateHrWorkflow",
                {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Training Assignment",
                        "status": "In Progress",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U302",
                    "message": "Your accelerated learning program has been initiated. Your course and goal progress have been updated, and your promotion workflow has been advanced.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "An accelerated learning program for Harper Bennett has been initiated. Her promotion workflow has advanced to the Training Assignment stage."
                },
            ),
        ],
        outputs=[
            "course progress updated",
            "workflow WF001 updated",
            "Goal G302-1 updated for user U302",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 35: Cross-functional analytics integration (Complexity: 12)
    Task(
        annotator="0",
        user_id="res_35",
        instruction="To facilitate Ava Nguyen's role in cross-functional integration, assign her to the 'Product Design Team'. Initiate a new 'Cross-functional Development' goal with ID 'G305-2' and description 'Master analytics-design integration'. Establish a mentorship with the first available mentor (reviewing M100-M103 by lowest workload, then by name) focusing on areas ['Product Marketing', 'Data Analytics', 'Design Thinking']. Inform her with the message: 'Your cross-functional development path has been established. You have been assigned to a new team, and a new goal and mentorship have been created.' and inform HR with the message: 'Ava Nguyen has been assigned to the Product Design Team to support cross-functional development. A new goal and mentorship have been established.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Harper", "last_name": "King"},
            ),
            Action("getTeamIdByName", {"team_name": "Product Design Team"}),
            Action("getTodayDate", {}),
            Action("addTeamMember", {"team_id": "T002", "user_id": "U305"}),
            Action(
                "addGoal",
                {
                    "user_id": "U305",
                    "goal": {
                        "goal_id": "G305-2",
                        "goal_type": "Cross-functional Development",
                        "goal_description": "Master analytics-design integration",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action("computeMentorLoad", {"mentor_id": "M100"}),
            Action("computeMentorLoad", {"mentor_id": "M101"}),
            Action("computeMentorLoad", {"mentor_id": "M102"}),
            Action("computeMentorLoad", {"mentor_id": "M103"}),
            Action(
                "addMentorshipRelationship",
                {
                    "mentor_id": "M103",
                    "mentee_id": "U305",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Product Marketing",
                        "Data Analytics",
                        "Design Thinking",
                    ],
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U305",
                    "message": "Your cross-functional development path has been established. You have been assigned to a new team, and a new goal and mentorship have been created.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Ava Nguyen has been assigned to the Product Design Team to support cross-functional development. A new goal and mentorship have been established."
                },
            ),
        ],
        outputs=[
            "User U305 added to team T002",
            "goal G305-2 added for U305",
            "Mentorship relationship MR011 created",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 36: Comprehensive certification strategy with goal alignment (Complexity: 13)
    Task(
        annotator="0",
        user_id="res_36",
        instruction="In order to define David Adams's path for PMP certification, enroll him in the 'Project Management Professional (PMP)' exam (cert ID 'C7015') taking place 230 days from today. Set up a new 'Certification' goal with ID 'G303-2' and description 'Achieve PMP certification'. Adjust his mentorship focus areas to incorporate 'PMP Certification Strategy'. Let him know with the message: 'Your PMP certification strategy has been established. You have been registered for the exam, and a new goal and mentorship focus have been created.' and let HR know with the message: 'A PMP certification strategy has been established for David Adams, including exam registration and a new development goal.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action("listUserMentorships", {"user_id": "U303"}),
            Action("getTodayDate", {}),
            Action(
                "addUserCertification",
                {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7015",
                        "cert_name": "Project Management Professional (PMP)",
                        "issuer": "PMI",
                        "scheduled_exam_date": "2026-05-20",
                    },
                },
            ),
            Action(
                "addGoal",
                {
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Certification",
                        "goal_description": "Achieve PMP certification",
                        "status": "Active",
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "PMP Certification Strategy",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U303",
                    "message": "Your PMP certification strategy has been established. You have been registered for the exam, and a new goal and mentorship focus have been created.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A PMP certification strategy has been established for David Adams, including exam registration and a new development goal."
                },
            ),
        ],
        outputs=[
            "Certification Project Management Professional (PMP) added for user U303",
            "goal G303-2 added for U303",
            "relationship MR006 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 37: Advanced accessibility leadership with UX enhancement (Complexity: 14)
    Task(
        annotator="0",
        user_id="res_37",
        instruction="To advance Alexander Adams towards a leadership role in accessibility, register her for the 'UX Design Fundamentals' course. Coordinate a mentorship session to occur 16 days from today. Adjust her mentorship focus areas to incorporate 'Advanced Accessibility Strategy'. Inform her with the message: 'Your pathway towards advanced accessibility leadership has been set. You are now enrolled in a new course, and a mentorship session is arranged.' Also, inform HR with the message: 'Alexander Adams's advanced accessibility leadership pathway is now established, including a new course enrollment and mentorship coordination.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action("getCourseIdByName", {"course_name": "UX Design Fundamentals"}),
            Action("listUserMentorships", {"user_id": "U307"}),
            Action("getTodayDate", {}),
            Action(
                "enrollInCourse",
                {"user_id": "U307", "course_id": "C1002", "enroll_date": "2025-10-02"},
            ),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR003", "session_date": "2025-10-18"},
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR003",
                    "updates": {
                        "focus_areas": [
                            "Accessibility",
                            "Mentorship",
                            "Design Leadership",
                            "Advanced Accessibility Strategy",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U307",
                    "message": "Your advanced accessibility leadership pathway has been established. You have been enrolled in a new course and a mentorship session has been scheduled.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "An advanced accessibility leadership pathway has been established for Alexander Adams, including new course enrollment and mentorship coordination."
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1002",
            '"scheduled_for": "2025-10-18"',
            "relationship MR003 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 38: Enterprise performance optimization with executive development (Complexity: 15)
    Task(
        annotator="0",
        user_id="res_38",
        instruction="To prepare Robert Thompson for enterprise-level performance, arrange an executive coaching session to take place 10 days from now. Modify his mentorship focus areas to add 'Executive Coaching'. Communicate with him using the message: 'To aid your enterprise-level performance objectives, an executive coaching session has been arranged and your mentorship plan is updated.' Additionally, inform HR with the message: 'An executive coaching session has been organized for Robert Thompson to further his enterprise-level performance objectives.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("listUserMentorships", {"user_id": "U306"}),
            Action("getTodayDate", {}),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR004", "session_date": "2025-10-12"},
            ),
            Action(
                "updateMentorshipRelationship",
                {
                    "relationship_id": "MR004",
                    "updates": {
                        "focus_areas": [
                            "Site Reliability Engineering",
                            "Leadership",
                            "Infrastructure",
                            "Executive Coaching",
                        ],
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U306",
                    "message": "To support your enterprise-level performance goals, an executive coaching session has been scheduled and your mentorship plan has been updated.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "An executive coaching session has been scheduled for Robert Thompson to support his enterprise-level performance goals."
                },
            ),
        ],
        outputs=[
            '"scheduled_for": "2025-10-12"',
            "relationship MR004 updated",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 39: Advanced coaching with strategic goal advancement (Complexity: 11)
    Task(
        annotator="0",
        user_id="res_39",
        instruction="Enhance Robert Thompson' primary career development goal by advancing its progress to 50%. Additionally, arrange a mentorship session set for 12 days from today to monitor his progress. Inform him with the message: 'Your career advancement goal has been updated. A new mentorship session has been scheduled to track your progress.' and inform HR with the message: 'Robert Thompson' primary career goal has been advanced and a new mentorship session has been scheduled.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action("listUserGoals", {"user_id": "U306"}),
            Action("listUserMentorships", {"user_id": "U306"}),
            Action("getTodayDate", {}),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR004", "session_date": "2025-10-14"},
            ),
            Action(
                "updateGoal",
                {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U306",
                    "message": "Your career advancement goal has been updated. A new mentorship session has been scheduled to track your progress.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "Robert Thompson' primary career goal has been advanced and a new mentorship session has been scheduled."
                },
            ),
        ],
        outputs=[
            '"scheduled_for": "2025-10-14"',
            "Goal G306-1 updated for user U306",
            "notified_user",
            '"notified": "HR"',
        ],
    ),
    # Task 40: Comprehensive skill validation with certification readiness (Complexity: 15)
    Task(
        annotator="0",
        user_id="res_40",
        instruction="To finalize David Adams's skill verification, increase his 'AWS Security' goal progress to 70%. Arrange a mentorship session for 20 days from today to verify certification readiness. Communicate to him with the message: 'Your skill validation is complete. Your goal progress has been updated, and a mentorship session has been scheduled to confirm certification readiness.' and communicate to HR with the message: 'A comprehensive skill validation for David Adams has been completed. His goal progress has been updated and a mentorship session is scheduled.'",
        actions=[
            Action(
                "getUserIdFromName",
                {"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(
                "getGoalIdByDescription",
                {"user_id": "U303", "keyword": "AWS Security"},
            ),
            Action("listUserMentorships", {"user_id": "U303"}),
            Action("getTodayDate", {}),
            Action(
                "updateGoal",
                {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 70,
                        "last_updated": "2025-10-02",
                    },
                },
            ),
            Action(
                "scheduleMentorshipSession",
                {"relationship_id": "MR006", "session_date": "2025-10-22"},
            ),
            Action(
                "notifyUser",
                {
                    "user_id": "U303",
                    "message": "Your skill validation is complete. Your goal progress has been updated, and a mentorship session has been scheduled to confirm certification readiness.",
                },
            ),
            Action(
                "notifyHr",
                {
                    "message": "A comprehensive skill validation for David Adams has been completed. His goal progress has been updated and a mentorship session is scheduled."
                },
            ),
        ],
        outputs=[
            "Goal G303-1 updated for user U303",
            '"scheduled_for": "2025-10-22"',
            "notified_user",
            '"notified": "HR"',
        ],
    ),
]
