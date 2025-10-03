# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "res_01",
        "instruction": "Ensure Jack Wang (U301) is registered for the Machine Learning course C1005 and update his promotion goal G301-1 to reflect the enrollment on 2025-10-02.",
        "actions": [
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U301"
                    }
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "getGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "U301 machine learning course enrollment completed"
                }
            }
        ],
        "outputs": [
                "User U301 enrolled in course C1005",
                "Goal G301-1 updated for user U301",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": pra-01,
        "user_id": "res_02",
        "instruction": "Place Ava Nguyen in the Analytics Team and set up a mentorship link with mentor M100, concentrating on analytics and career advancement. Next, inform him with this message: 'Welcome to the Analytics Team! You have been assigned a mentor to support your career growth.', and then inform HR with the following message: 'Ava Nguyen has been added to the Analytics Team and assigned mentor.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Harper",
                    "last_name": "King"
                },
            },
            {
                "name": "addTeamMember",
                "arguments": {
                    "team_id": "T001",
                    "user_id": "U305"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M100"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "addMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M100",
                    "mentee_id": "U305",
                    "status": "Active",
                    "start_date": "2025-10-02",
                    "focus_areas": [
                        "Analytics",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U305",
                    "message": "Welcome to the Analytics Team! You have been assigned a mentor to support your career growth."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Ava Nguyen has been added to the Analytics Team and assigned mentor."
                }
            }
        ],
        "outputs": [
                "User U305 added to team T001",
                "Mentorship relationship MR011 created",
                "notified_user",
                "notified"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_03",
        "instruction": "Assign Alexander Adams to a foundational UX course to boost her skills and update her development goal with 'Active - Course Assigned'. Afterwards, send her a notification with the message: 'You have been enrolled in the 'UX Design Fundamentals' course to support your development goals.', and then inform hr with the message: 'Alexander Adams has been enrolled in course UX Design Fundamentals'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U307",
                    "course_id": "C1002",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "status": "Active - Course Assigned",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "getCourse",
                "arguments": {
                    "course_id": "C1002"
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U307",
                    "message": "You have been enrolled in the 'UX Design Fundamentals' course to support your development goals."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Alexander Adams has been enrolled in course UX Design Fundamentals."
                }
            }
        ],
        "outputs": [
                "User U307 enrolled in course C1002",
                "Goal G307-1 updated for user U307",
                "notified_user",
                "notified"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_04",
        "instruction": "Set up the next mentorship session for David Adams (U304) two weeks from today on 2025-10-16. Inform him with the message: 'Your next mentorship session has been scheduled. Please check your calendar for details.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR002",
                    "session_date": "2025-10-16"
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR002",
                    "updates": {
                        "next_session_date": "2025-10-16"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "Your next mentorship session has been scheduled. Please check your calendar for details."
                }
            }
        ],
        "outputs": [
                "\"scheduled_for\": \"2025-10-16\"",
                "relationship MR002 updated",
                "notified_user"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_05",
        "instruction": "Handle the registration of the 'AWS Security Specialty' certification from 'AWS' for David Adams, assigning a new certification ID 'C7011' and set up the exam for 60 days from today. Modify his certification goal to denote a 10% advancement. Inform HR through the message: 'David Adams (U303) has registered for the AWS Security Specialty exam.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U303"
                    }
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7011",
                        "cert_name": "AWS Security Specialty",
                        "issuer": "AWS",
                        "issue_date": null,
                        "scheduled_exam_date": "2025-12-01"
                    }
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 10,
                        "status": "In Progress - Exam Scheduled",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "David Adams (U303) has registered for the AWS Security Specialty exam."
                }
            }
        ],
        "outputs": [
                "Certification AWS Security Specialty added for user U303",
                "Goal G303-1 updated for user U303",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_06",
        "instruction": "Update Harper Bennett's 'Python' course progress to 50%. Additionally, adjust the 'last_updated' field concerning her career goal related to 'Python'. Finally, send a notification to her with the message: 'Your progress on the Python course has been updated to 50%. Keep up the great work!' and alert HR with the message: 'Harper Bennett has reached a 50% progress milestone in her Python course, supporting her development goal.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Python"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U302",
                    "keyword": "Python"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateUserCourseProgress",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "updates": {
                        "current_progress_percent": 50
                    }
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "Your progress on the Python course has been updated to 50%. Keep up the great work!"
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Harper Bennett has reached a 50% progress milestone in her Python course, supporting her development goal."
                }
            }
        ],
        "outputs": [
                "course progress updated",
                "Goal G302-1 updated for user U302",
                "notified_user",
                "notified"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_07",
        "instruction": "Progress Harper Bennett's promotion workflow to the 'Development Plan' phase. Determine who the designated planner is for this stage, find out their full name, and update the workflow notes to indicate their assignment. Enroll Ava in the course recommended by the workflow. Additionally, update her career goal related to 'Python' by including: 'Development plan now active under WF001.' in the description. Notify Ava with the message: 'Your promotion workflow has progressed to the Development Plan stage and you have been enrolled in required training.' and inform the assigned planner with the message: 'You have been designated as the planner for Harper Bennett's development plan in promotion workflow WF001.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "findHrWorkflowForUser",
                "arguments": {
                    "user_id": "U302"
                },
            },
            {
                "name": "getHrWorkflow",
                "arguments": {
                    "workflow_id": "WF001"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U310"
                    }
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U302",
                    "keyword": "Python"
                },
            },
            {
                "name": "getGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateHrWorkflow",
                "arguments": {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "notes_append": "Plan assigned to planner Alexander Adams.",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "goal_description": "Add Python to clinical-analytics toolkit and deliver an internal POC to demonstrate leadership in data-driven decision making. Development plan now active under WF001.",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "Your promotion workflow has advanced to the Development Plan stage and you have been enrolled in required training."
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U310",
                    "message": "You have been assigned as the planner for Harper Bennett's development plan in promotion workflow WF001."
                }
            }
        ],
        "outputs": [
                "workflow WF001 updated",
                "User U302 enrolled in course C1005",
                "Goal G302-1 updated for user U302",
                "notified_user",
                "notified_user"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_08",
        "instruction": "Initially, confirm that Robert Thompson satisfies the '3+ years PM experience' requirement for the 'Project Management Professional (PMP)' course. If he does, proceed to enroll him. Then, update his goal related to 'Staff SRE' by appending the note: 'PMP course enrolled to support leadership path.' Moreover, update his mentorship relationship by adding 'Strategic Leadership' to the current focus areas. Finally, notify both Alexander and his manager about the enrollment using the message: 'Robert Thompson has been enrolled in the PMP course to support his strategic development goals.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U306"
                    }
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "getCourse",
                "arguments": {
                    "course_id": "C1004"
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1004",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "goal_description": "Advance to Staff Site Reliability Engineer and lead reliability roadmap. PMP course enrolled to support leadership path.",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR004",
                    "updates": {
                        "focus_areas": [
                            "Site Reliability Engineering",
                            "Leadership",
                            "Infrastructure",
                            "Strategic Leadership"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U306",
                    "message": "Robert Thompson has been enrolled in the PMP course to support his strategic development goals."
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U312",
                    "message": "Robert Thompson has been enrolled in the PMP course to support his strategic development goals."
                }
            }
        ],
        "outputs": [
                "User U306 enrolled in course C1004",
                "Goal G306-1 updated for user U306",
                "relationship MR004 updated",
                "notified_user",
                "notified_user"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_09",
        "instruction": "Facilitate David Adams's growth by enrolling him in the 'Data Visualization with Tableau' course. Modify his primary goal metric associated with 'AWS Security' to include 'Pass AWS Security Specialty exam and complete Tableau course'. Additionally, revise his mentorship details by incorporating 'Data Visualization' into the focus areas. Inform him with the message: 'You have been enrolled in a Tableau course as a foundational step towards your AWS Security goal, which has been updated to reflect this.' and alert HR with the message: 'David Adams has been enrolled in supplemental Tableau training to support his primary AWS Security goal.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U303",
                    "keyword": "AWS Security"
                },
            },
            {
                "name": "getGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "metric": "Pass AWS Security Specialty exam and complete Tableau course",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Career Transition",
                            "Data Visualization"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U303",
                    "message": "You have been enrolled in a Tableau course as a foundational step towards your AWS Security goal, which has been updated to reflect this."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "David Adams has been enrolled in supplemental Tableau training to support his primary AWS Security goal."
                }
            }
        ],
        "outputs": [
                "User U303 enrolled in course C1003",
                "Goal G303-1 updated for user U303",
                "relationship MR006 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_10",
        "instruction": "Place Alexander Adams on the 'Product Design Team'. Augment her primary career goal by adding the note: 'Now a member of the Product Design Team to lead accessibility initiatives.' Arrange a mentorship session for the following week. Inform Chloe with the message: 'You have been assigned to the Product Design Team to lead accessibility initiatives. Your career goal has been updated and a mentorship session is scheduled.' Also, notify her new manager and HR with the message: 'Alexander Adams has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getTeamIdByName",
                "arguments": {
                    "team_name": "Product Design Team"
                },
            },
            {
                "name": "getTeam",
                "arguments": {
                    "team_id": "T002"
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "addTeamMember",
                "arguments": {
                    "team_id": "T002",
                    "user_id": "U307"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "goal_description": "Publish company-wide accessibility guidelines and train designers. Now a member of the Product Design Team to lead accessibility initiatives.",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR003",
                    "session_date": "2025-10-09"
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U307",
                    "message": "You have been assigned to the Product Design Team to lead accessibility initiatives. Your career goal has been updated and a mentorship session is scheduled."
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "Alexander Adams has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Alexander Adams has been assigned to the Product Design Team to lead accessibility initiatives. Her development plan has been updated."
                }
            }
        ],
        "outputs": [
                "User U307 added to team T002",
                "Goal G307-1 updated for user U307",
                "\"scheduled_for\": \"2025-10-09\"",
                "notified_user",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_11",
        "instruction": "Facilitate Ava Nguyen's development by enrolling him in the 'Machine Learning Specialization' course. Revise his goal concerning 'Director of Data Science' to incorporate this enrollment by adding 'and complete ML Specialization' to its metric. Additionally, augment his mentorship relationship by including 'Machine Learning' in the current focus areas. Inform him with the message: 'You have been enrolled in the ML Specialization as a step towards your Director goal, which has been updated to reflect this.' and inform HR with the message: 'Ava Nguyen has been enrolled in supplemental ML training to support his primary promotion goal.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U301",
                    "keyword": "Director of Data Science"
                },
            },
            {
                "name": "getGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "metric": "Complete ML course and publish 2 predictive models and complete ML Specialization",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Machine Learning"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U301",
                    "message": "You have been enrolled in the ML Specialization as a step towards your Director goal, which has been updated to reflect this."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Ava Nguyen has been enrolled in supplemental ML training to support his primary promotion goal."
                }
            }
        ],
        "outputs": [
                "User U301 enrolled in course C1005",
                "Goal G301-1 updated for user U301",
                "relationship MR001 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_12",
        "instruction": "Facilitate Michael Rodriguez' performance enhancement by enrolling him in the 'UX Design Fundamentals' course. Establish a new 'Skill Development' goal for him with ID 'G304-2' and description 'Complete UX Design Fundamentals to strengthen technical foundations'. Strengthen his mentorship relationship by adding 'Technical Foundation Support' to the focus areas. Inform him with the message: 'A performance support plan has been initiated. You have been enrolled in a foundational course and a new goal has been set. Please connect with your mentor.' and inform HR with the message: 'A performance support plan has been activated for Michael Rodriguez, including course enrollment and a new development goal.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1002",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "addGoal",
                "arguments": {
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-2",
                        "goal_type": "Skill Development",
                        "status": "Active",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": "Technical Foundation Support",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "A performance support plan has been initiated. You have been enrolled in a foundational course and a new goal has been set. Please connect with your mentor."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A performance support plan has been activated for Michael Rodriguez, including course enrollment and a new development goal."
                }
            }
        ],
        "outputs": [
                "User U304 enrolled in course C1002",
                "goal G304-2 added for U304",
                "relationship MR002 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_13",
        "instruction": "To bridge skill gaps, register Harper Bennett for the 'Machine Learning Specialization' course. Modify her goal associated with 'Python' to incorporate this new training. Additionally, create a new mentorship link for her by choosing the first available mentor (starting alphabetically from M100) concentrating on 'Machine Learning'. Inform her with the message: 'To support your career advancement, you have been enrolled in the Machine Learning Specialization course and assigned a new mentor.' and inform HR with the message: 'Harper Bennett has been enrolled in targeted ML training and assigned a mentor to address identified skill gaps.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U302",
                    "keyword": "Python"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M100"
                },
            },
            {
                "name": "addMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M100",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Machine Learning"
                    ]
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "To support your career advancement, you have been enrolled in the Machine Learning Specialization course and assigned a new mentor."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Harper Bennett has been enrolled in targeted ML training and assigned a mentor to address identified skill gaps."
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1005",
                "Goal G302-1 updated for user U302",
                "Mentorship relationship MR011 created",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_14",
        "instruction": "In order to enhance David Adams's technical skills, register him for the 'Advanced Python' course. Change his goal concerning 'AWS Security' by setting its completion date to 90 days from now. Moreover, revise his mentorship engagement to set the focus areas to Cloud Security, Compliance, and Python Development. Inform him with the message: 'To support your technical development, you have been enrolled in the Advanced Python course. Your AWS certification goal and mentorship plan have been updated accordingly.' and inform HR with the message: 'David Adams has been enrolled in Python training to complement his cloud security goals. His development plan has been updated.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U303",
                    "keyword": "AWS Security"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "target_date": "2025-12-31",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Python Development"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U303",
                    "message": "To support your technical development, you have been enrolled in the Advanced Python course. Your AWS certification goal and mentorship plan have been updated accordingly."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "David Adams has been enrolled in Python training to complement his cloud security goals. His development plan has been updated."
                }
            }
        ],
        "outputs": [
                "User U303 enrolled in course C1001",
                "Goal G303-1 updated for user U303",
                "relationship MR006 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_15",
        "instruction": "In order to prepare Michael Rodriguez for certification, modify his primary career objective related to 'DesignOps' by adding the note: 'This goal is supported by pursuing AWS Solutions Architect certification.' Register him for the 'AWS Solutions Architect Associate' exam (cert ID 'C7012') happening in 180 days. Additionally, adjust his mentorship focus areas to encompass 'AWS Certification Prep'. Inform him with the message: 'A new development path has been created for you to pursue AWS certification. Your primary career goal and mentorship plan have been updated.' and inform HR with the message: 'A certification path for AWS Solutions Architect Associate has been established for Michael Rodriguez.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U304",
                    "keyword": "DesignOps"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U304",
                    "cert": {
                        "cert_id": "C7012",
                        "cert_name": "AWS Solutions Architect Associate",
                        "issuer": "AWS",
                        "scheduled_exam_date": "2026-03-31"
                    }
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U304",
                    "goal_id": "G304-1",
                    "updates": {
                        "goal_description": "Move into DesignOps Lead role and formalize cross-team processes. This goal is supported by pursuing AWS Solutions Architect certification.",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "AWS Certification Prep"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "A new development path has been created for you to pursue AWS certification. Your primary career goal and mentorship plan have been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A certification path for AWS Solutions Architect Associate has been established for Michael Rodriguez."
                }
            }
        ],
        "outputs": [
                "Certification AWS Solutions Architect Associate added for user U304",
                "Goal G304-1 updated for user U304",
                "relationship MR002 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_16",
        "instruction": "To improve mentor capacity, transfer Alexander Adams to a different mentor. The replacement mentor must be the one with the fewest current mentees (checking M101, M102, and M103), with alphabetical order used as a tiebreaker. The new relationship should maintain the focus areas from the previous one. The prior relationship should be labeled as 'Inactive - Reassigned'. Notify Chloe with the message: 'To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.' and inform HR with the message: 'Mentor load balancing has been performed. Alexander Adams has been reassigned to a new mentor.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M101"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M102"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M103"
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR003",
                    "updates": {
                        "status": "Inactive - Reassigned",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "addMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M103",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Accessibility",
                        "Mentorship",
                        "Design Leadership"
                    ]
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U307",
                    "message": "To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Mentor load balancing has been performed. Alexander Adams has been reassigned to a new mentor."
                }
            }
        ],
        "outputs": [
                "relationship MR003 updated",
                "Mentorship relationship MR011 created",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_17",
        "instruction": "To verify Harper Bennett's capability in data visualization, sign her up for the 'Data Visualization with Tableau' course. Initiate a new 'Skill Development' goal for her using ID 'G302-2' and include the description 'Achieve proficiency in Tableau for clinical analytics'. Also, set up a new mentorship for her with the available mentor found by checking M100-M103, prioritized by the lowest workload, then alphabetically, focusing on Clinical Analytics, Python, and Tableau. Inform her with the message: 'A new development path has been created for you to master data visualization. You have been enrolled in a Tableau course, and a new goal and mentorship have been established.' and alert HR with the message: 'Harper Bennett has been enrolled in Tableau training with a new goal and mentorship to support her data visualization competency.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "addGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-2",
                        "goal_type": "Skill Development",
                        "goal_description": "Achieve proficiency in Tableau for clinical analytics",
                        "status": "Active",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M100"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M101"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M102"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M103"
                },
            },
            {
                "name": "addMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M103",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Clinical Analytics",
                        "Python",
                        "Tableau"
                    ]
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "A new development path has been created for you to master data visualization. You have been enrolled in a Tableau course, and a new goal and mentorship have been established."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Harper Bennett has been enrolled in Tableau training with a new goal and mentorship to support her data visualization competency."
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1003",
                "goal G302-2 added for U302",
                "Mentorship relationship MR014 created",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_18",
        "instruction": "To confirm the progress of David Adams's AWS Security goal, register him in the 'Advanced Python' course. Adjust his 'AWS Security' goal progress to reflect 25%. Arrange for a mentorship session to occur 14 days from today. Inform him with the message: 'Your AWS Security goal progress has been updated. You have been enrolled in a new course and a mentorship session has been scheduled to discuss your technical advancement.' and alert HR with the message: 'David Adams's AWS Security goal has been updated with a new course enrollment and a scheduled mentorship session.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U303",
                    "keyword": "AWS Security"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 25,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR006",
                    "session_date": "2025-10-16"
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U303",
                    "message": "Your AWS Security goal progress has been updated. You have been enrolled in a new course and a mentorship session has been scheduled to discuss your technical advancement."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "David Adams's AWS Security goal has been updated with a new course enrollment and a scheduled mentorship session."
                }
            }
        ],
        "outputs": [
                "User U303 enrolled in course C1001",
                "Goal G303-1 updated for user U303",
                "\"scheduled_for\": \"2025-10-16\"",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_19",
        "instruction": "Handle Michael Rodriguez' preparation for cross-functional leadership by enrolling him in the 'Machine Learning Specialization' program. Introduce a new 'Leadership' goal with the ID 'G304-2', described as 'Lead a cross-functional design project leveraging ML insights'. Update his mentorship focus areas to ['Design Operations', 'Leadership', 'Process Management', 'Cross-functional Collaboration']. Inform him with the message: 'To support your growth into cross-functional leadership, you have been enrolled in a Machine Learning course and a new leadership goal has been created.' and inform HR with the message: 'Michael Rodriguez has been enrolled in ML training to support a new cross-functional leadership goal.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "addGoal",
                "arguments": {
                    "user_id": "U304",
                    "goal": {
                        "goal_id": "G304-2",
                        "goal_type": "Leadership",
                        "goal_description": "Lead a cross-functional design project leveraging ML insights",
                        "status": "Active",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Cross-functional Collaboration"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "To support your growth into cross-functional leadership, you have been enrolled in a Machine Learning course and a new leadership goal has been created."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Michael Rodriguez has been enrolled in ML training to support a new cross-functional leadership goal."
                }
            }
        ],
        "outputs": [
                "User U304 enrolled in course C1005",
                "goal G304-2 added for U304",
                "relationship MR002 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_20",
        "instruction": "Coordinate the creation of a strategic development plan for Michael Rodriguez by enrolling him in the 'Agile Product Management' course. Update his mentorship focus areas by adding 'Agile Methodologies'. Arrange a mentorship session to occur 14 days from today. Inform him with the message: 'A new strategic development plan has been initiated. You have been enrolled in an Agile course, and a mentorship session has been scheduled to discuss next steps.' and inform HR with the message: 'A strategic development plan has been established for Michael Rodriguez, including Agile course enrollment and mentorship alignment.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Agile Product Management"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1006",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR002",
                    "session_date": "2025-10-16"
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Agile Methodologies"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "A new strategic development plan has been initiated. You have been enrolled in an Agile course, and a mentorship session has been scheduled to discuss next steps."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A strategic development plan has been established for Michael Rodriguez, including Agile course enrollment and mentorship alignment."
                }
            }
        ],
        "outputs": [
                "User U304 enrolled in course C1006",
                "\"scheduled_for\": \"2025-10-16\"",
                "relationship MR002 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_21",
        "instruction": "Ensure Ava Nguyen's ML skills by registering him for the 'Machine Learning Specialization' course. Adjust his goal concerning the Director of Data Science to a 45% completion rate. Additionally, modify his mentorship relationship to highlight Leadership, Data Science, Career Growth, and Machine Learning as focus areas. Inform HR with the message: 'Ava Nguyen has been enrolled in the Machine Learning Specialization to validate competency for his promotion goal. His development plan has been updated.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U301",
                    "keyword": "Director of Data Science"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Machine Learning"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Ava Nguyen has been enrolled in the Machine Learning Specialization to validate competency for his promotion goal. His development plan has been updated."
                }
            }
        ],
        "outputs": [
                "User U301 enrolled in course C1005",
                "Goal G301-1 updated for user U301",
                "relationship MR001 updated",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_22",
        "instruction": "Create a development plan for Harper Bennett by moving her promotion workflow to the 'Development Plan' phase and scheduling a review date 60 days from now. Enroll her in the 'Machine Learning Specialization' and 'Data Visualization with Tableau' courses. Modify her goal associated with 'Python' to show 40% progress. Communicate to her with the message: 'Your development plan has been established. You have been enrolled in new courses to support your promotion goals.' and notify HR with the message: 'A development plan for Harper Bennett has been established, including new course enrollments and a scheduled review date.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "findHrWorkflowForUser",
                "arguments": {
                    "user_id": "U302"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U302",
                    "keyword": "Python"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateHrWorkflow",
                "arguments": {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "review_date": "2025-12-01",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 40,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "Your development plan has been established. You have been enrolled in new courses to support your promotion goals."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A development plan for Harper Bennett has been established, including new course enrollments and a scheduled review date."
                }
            }
        ],
        "outputs": [
                "workflow WF001 updated",
                "User U302 enrolled in course C1005",
                "User U302 enrolled in course C1003",
                "Goal G302-1 updated for user U302",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_23",
        "instruction": "In order to groom Alexander Adams for a leadership position, register her in the 'Agile Product Management' course. Amend her primary goal relating to accessibility to add the note: 'and master Agile methodologies for future leadership roles.' Additionally, modify her mentorship focus areas to encompass 'Agile Leadership'. Inform Chloe, her manager, and HR with the message: 'A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U307"
                    }
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Agile Product Management"
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U307",
                    "course_id": "C1006",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "updates": {
                        "goal_description": "Publish company-wide accessibility guidelines and train designers. and master Agile methodologies for future leadership roles.",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR003",
                    "updates": {
                        "focus_areas": [
                            "Accessibility",
                            "Mentorship",
                            "Design Leadership",
                            "Agile Leadership"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U307",
                    "message": "A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this."
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A new leadership development plan has been initiated for Alexander Adams. She has been enrolled in Agile training, and her career goal and mentorship plan have been updated to support this."
                }
            }
        ],
        "outputs": [
                "User U307 enrolled in course C1006",
                "Goal G307-1 updated for user U307",
                "relationship MR003 updated",
                "notified_user",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_24",
        "instruction": "To carve out a post-MBA strategic leadership route for David Adams, sign him up for the 'Project Management Professional (PMP)' certification (cert ID 'C7014') with an exam scheduled 225 days from today. Enlist him in the 'Agile Product Management' course. Establish a new 'Leadership' goal with ID 'G303-2' and description 'Achieve PMP certification and demonstrate strategic leadership'. Revise his mentorship focus areas to include 'Strategic Leadership'. Communicate to him with the message: 'Your post-MBA leadership pathway has been established. You have been registered for the PMP exam, enrolled in a new course, and a new goal has been created.' and inform HR with the message: 'A post-MBA strategic leadership pathway has been established for David Adams, including PMP registration and a new development goal.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Agile Product Management"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7014",
                        "cert_name": "Project Management Professional (PMP)",
                        "issuer": "PMI",
                        "scheduled_exam_date": "2026-05-14"
                    }
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1006",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "addGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Leadership",
                        "goal_description": "Achieve PMP certification and demonstrate strategic leadership",
                        "status": "Active",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "Strategic Leadership"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U303",
                    "message": "Your post-MBA leadership pathway has been established. You have been registered for the PMP exam, enrolled in a new course, and a new goal has been created."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A post-MBA strategic leadership pathway has been established for David Adams, including PMP registration and a new development goal."
                }
            }
        ],
        "outputs": [
                "Certification Project Management Professional (PMP) added for user U303",
                "User U303 enrolled in course C1006",
                "goal G303-2 added for U303",
                "relationship MR006 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_25",
        "instruction": "Handle the enhancement of Michael Rodriguez' stakeholder management skills by enrolling him in the 'Project Management Professional (PMP)' course. Amend his mentorship focus areas to encompass 'Stakeholder Alignment'. Inform him with the message: 'To advance your stakeholder management competency, you have been enrolled in a leadership course and your mentorship plan has been updated.' and alert HR with the message: 'Michael Rodriguez has been enrolled in leadership training to support his stakeholder management competency.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Project Management Professional (PMP)"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1004",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR002",
                    "updates": {
                        "focus_areas": [
                            "Design Operations",
                            "Leadership",
                            "Process Management",
                            "Stakeholder Alignment"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U304",
                    "message": "To advance your stakeholder management competency, you have been enrolled in a leadership course and your mentorship plan has been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Michael Rodriguez has been enrolled in leadership training to support his stakeholder management competency."
                }
            }
        ],
        "outputs": [
                "User U304 enrolled in course C1004",
                "relationship MR002 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_26",
        "instruction": "Coordinate the acceleration of Harper Bennett's foundation skills by enrolling her in the 'Advanced Python' course. Update her progress related to 'Python' by adjusting it to 10%. Inform her with the message: 'To accelerate your foundation skills, you have been enrolled in the Advanced Python course and your goal progress has been updated.' and notify HR with the message: 'Harper Bennett has been enrolled in Python training to accelerate her foundation skills. Her goal progress has been synchronized.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U302",
                    "keyword": "Python"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 10,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "To accelerate your foundation skills, you have been enrolled in the Advanced Python course and your goal progress has been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Harper Bennett has been enrolled in Python training to accelerate her foundation skills. Her goal progress has been synchronized."
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1001",
                "Goal G302-1 updated for user U302",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_27",
        "instruction": "To enhance mentor capacity for Mentor M100, reassign their latest mentee, Alexander Adams, to a different mentor. Choose the new mentor with the lowest current mentee count from M101, M102, and M103, using an alphabetical order if needed to decide ties. Ensure the new relationship retains the focus areas of the previous one. Label the previous relationship as 'Inactive - Reassigned'. Inform Chloe with the message: 'To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details.' and notify HR with the message: 'Mentor load balancing has been performed. Alexander Adams has been reassigned from Mentor M100 to a new mentor to optimize capacity.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M101"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M102"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M103"
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR003",
                    "updates": {
                        "status": "Inactive - Reassigned",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "addMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M103",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Accessibility",
                        "Mentorship",
                        "Design Leadership"
                    ]
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U307",
                    "message": "To ensure you continue to receive quality support, your mentorship has been reassigned to a new mentor. Please check your profile for details."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Mentor load balancing has been performed. Alexander Adams has been reassigned from Mentor M100 to a new mentor to optimize capacity."
                }
            }
        ],
        "outputs": [
                "relationship MR003 updated",
                "Mentorship relationship MR011 created",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_28",
        "instruction": "To fill Harper Bennett's skill gaps, register her in the 'Machine Learning Specialization' course. Align her 'Python' goal by updating its progress to 15%. Inform her with the message: 'To address your skill gaps, you have been enrolled in the Machine Learning Specialization and your goal progress has been updated.' and notify HR with the message: 'Harper Bennett has been enrolled in ML training to address identified skill gaps. Her goal progress has been synchronized.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U302",
                    "keyword": "Python"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 15,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "To address your skill gaps, you have been enrolled in the Machine Learning Specialization and your goal progress has been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Harper Bennett has been enrolled in ML training to address identified skill gaps. Her goal progress has been synchronized."
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1005",
                "Goal G302-1 updated for user U302",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_29",
        "instruction": "Handle the synchronization of Ava Nguyen's 'Director of Data Science' goal by aligning its progress with his current average course completion rate. Should the updated progress exceed 50%, arrange a review meeting with his mentor for the following week. Inform Jack of the goal update, and should a session be arranged, include this detail in his notification and also inform his mentor.",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U301",
                    "keyword": "Director of Data Science"
                },
            },
            {
                "name": "computeAverageProgress",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 72.5,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR001",
                    "session_date": "2025-10-09"
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U301",
                    "message": "Your Director promotion goal has been updated to 72.5% based on your average course progress. A review session with your mentor has been scheduled for 2025-10-09."
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "M102",
                    "message": "A progress review session with your mentee, Ava Nguyen, has been scheduled for 2025-10-09 to discuss his recent goal advancement."
                }
            }
        ],
        "outputs": [
                "Goal G301-1 updated for user U301",
                "\"scheduled_for\": \"2025-10-09\"",
                "notified_user",
                "notified_user"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_30",
        "instruction": "Coordinate Ava Nguyen's advancement in analytics by registering him for the 'Data Visualization with Tableau' course. Keep track of this by adjusting his 'Director of Data Science' goal progress to 50%. Notify him with the message: 'To enhance your analytics mastery, you have been enrolled in a Tableau course and your goal progress has been updated.' and inform HR with the message: 'Ava Nguyen has been enrolled in supplemental Tableau training to support his analytics mastery. His goal progress has been updated.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U301",
                    "keyword": "Director of Data Science"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U301",
                    "message": "To enhance your analytics mastery, you have been enrolled in a Tableau course and your goal progress has been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Ava Nguyen has been enrolled in supplemental Tableau training to support his analytics mastery. His goal progress has been updated."
                }
            }
        ],
        "outputs": [
                "User U301 enrolled in course C1003",
                "Goal G301-1 updated for user U301",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_31",
        "instruction": "Ensure Harper Bennett's promotion workflow is advanced to Development Plan with verification of Skills Assessment completion and initiation of ML course enrollment.",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U302"
                    }
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "getHrWorkflow",
                "arguments": {
                    "workflow_id": "WF001"
                },
            },
            {
                "name": "updateHrWorkflow",
                "arguments": {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Development Plan",
                        "status": "In Progress",
                        "skills_assessment_completed": "2025-10-02"
                    }
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "getGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "WF001 progression to Development Plan completed"
                }
            }
        ],
        "outputs": [
                "workflow WF001 updated",
                "User U302 enrolled in course C1005",
                "Goal G302-1 updated for user U302",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_32",
        "instruction": "In order to complete Robert Thompson' leadership development, confirm that his primary goal associated with 'Staff SRE' is recorded as 100% finished, and add the note 'Final leadership milestone achieved.' to its description. Arrange a concluding coaching session with his mentor for the coming week. Inform Alexander, his mentor, and HR by sending the message: 'Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 100,
                        "status": "Completed",
                        "goal_description": "Advance to Staff Site Reliability Engineer and lead reliability roadmap. Final leadership milestone achieved.",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR004",
                    "session_date": "2025-10-09"
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U306",
                    "message": "Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan."
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "M101",
                    "message": "Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Robert Thompson has successfully completed his Staff SRE leadership goal. A final coaching session has been scheduled to conclude his development plan."
                }
            }
        ],
        "outputs": [
                "Goal G306-1 updated for user U306",
                "\"scheduled_for\": \"2025-10-09\"",
                "notified_user",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_33",
        "instruction": "Upon the completion of his quarterly performance review, adjust Ava Nguyen's goal for the 'Director of Data Science' by updating its progress to 65%. Inform him with the message: 'Your quarterly performance review has been completed and your promotion goal progress has been updated.' and alert HR with the message: 'The quarterly performance review for Ava Nguyen is complete. His promotion goal has been updated accordingly.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "searchUsers",
                "arguments": {
                    "filters": {
                        "user_id": "U301"
                    }
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U301",
                    "keyword": "Director of Data Science"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "updates": {
                        "progress_percent": 65,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U301",
                    "message": "Your quarterly performance review has been completed and your promotion goal progress has been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "The quarterly performance review for Ava Nguyen is complete. His promotion goal has been updated accordingly."
                }
            }
        ],
        "outputs": [
                "Goal G301-1 updated for user U301",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_34",
        "instruction": "Conduct an accelerated learning program initiation for Harper Bennett by adjusting her 'Advanced Python' course progress to 25%. Move her promotion workflow to the 'Training Assignment' phase. Modify her goal related to 'Python' to reflect 45% progress. Inform her with the message: 'Your accelerated learning program has been initiated. Your course and goal progress have been updated, and your promotion workflow has been advanced.' and alert HR with the message: 'An accelerated learning program for Harper Bennett has been initiated. Her promotion workflow has advanced to the Training Assignment stage.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "findHrWorkflowForUser",
                "arguments": {
                    "user_id": "U302"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U302",
                    "keyword": "Python"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateUserCourseProgress",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "updates": {
                        "current_progress_percent": 25,
                        "status": "In Progress"
                    }
                },
            },
            {
                "name": "updateHrWorkflow",
                "arguments": {
                    "workflow_id": "WF001",
                    "updates": {
                        "current_stage": "Training Assignment",
                        "status": "In Progress",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "updates": {
                        "progress_percent": 45,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U302",
                    "message": "Your accelerated learning program has been initiated. Your course and goal progress have been updated, and your promotion workflow has been advanced."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "An accelerated learning program for Harper Bennett has been initiated. Her promotion workflow has advanced to the Training Assignment stage."
                }
            }
        ],
        "outputs": [
                "course progress updated",
                "workflow WF001 updated",
                "Goal G302-1 updated for user U302",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_35",
        "instruction": "To facilitate Ava Nguyen's role in cross-functional integration, assign her to the 'Product Design Team'. Initiate a new 'Cross-functional Development' goal with ID 'G305-2' and description 'Master analytics-design integration'. Establish a mentorship with the first available mentor (reviewing M100-M103 by lowest workload, then by name) focusing on areas ['Product Marketing', 'Data Analytics', 'Design Thinking']. Inform her with the message: 'Your cross-functional development path has been established. You have been assigned to a new team, and a new goal and mentorship have been created.' and inform HR with the message: 'Ava Nguyen has been assigned to the Product Design Team to support cross-functional development. A new goal and mentorship have been established.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Harper",
                    "last_name": "King"
                },
            },
            {
                "name": "getTeamIdByName",
                "arguments": {
                    "team_name": "Product Design Team"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "addTeamMember",
                "arguments": {
                    "team_id": "T002",
                    "user_id": "U305"
                },
            },
            {
                "name": "addGoal",
                "arguments": {
                    "user_id": "U305",
                    "goal": {
                        "goal_id": "G305-2",
                        "goal_type": "Cross-functional Development",
                        "goal_description": "Master analytics-design integration",
                        "status": "Active",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M100"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M101"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M102"
                },
            },
            {
                "name": "computeMentorLoad",
                "arguments": {
                    "mentor_id": "M103"
                },
            },
            {
                "name": "addMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M103",
                    "mentee_id": "U305",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Product Marketing",
                        "Data Analytics",
                        "Design Thinking"
                    ]
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U305",
                    "message": "Your cross-functional development path has been established. You have been assigned to a new team, and a new goal and mentorship have been created."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Ava Nguyen has been assigned to the Product Design Team to support cross-functional development. A new goal and mentorship have been established."
                }
            }
        ],
        "outputs": [
                "User U305 added to team T002",
                "goal G305-2 added for U305",
                "Mentorship relationship MR011 created",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_36",
        "instruction": "In order to define David Adams's path for PMP certification, enroll him in the 'Project Management Professional (PMP)' exam (cert ID 'C7015') taking place 230 days from today. Set up a new 'Certification' goal with ID 'G303-2' and description 'Achieve PMP certification'. Adjust his mentorship focus areas to incorporate 'PMP Certification Strategy'. Let him know with the message: 'Your PMP certification strategy has been established. You have been registered for the exam, and a new goal and mentorship focus have been created.' and let HR know with the message: 'A PMP certification strategy has been established for David Adams, including exam registration and a new development goal.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "addUserCertification",
                "arguments": {
                    "user_id": "U303",
                    "cert": {
                        "cert_id": "C7015",
                        "cert_name": "Project Management Professional (PMP)",
                        "issuer": "PMI",
                        "scheduled_exam_date": "2026-05-20"
                    }
                },
            },
            {
                "name": "addGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Certification",
                        "goal_description": "Achieve PMP certification",
                        "status": "Active",
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR006",
                    "updates": {
                        "focus_areas": [
                            "Cloud Security",
                            "Compliance",
                            "PMP Certification Strategy"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U303",
                    "message": "Your PMP certification strategy has been established. You have been registered for the exam, and a new goal and mentorship focus have been created."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A PMP certification strategy has been established for David Adams, including exam registration and a new development goal."
                }
            }
        ],
        "outputs": [
                "Certification Project Management Professional (PMP) added for user U303",
                "goal G303-2 added for U303",
                "relationship MR006 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_37",
        "instruction": "To advance Alexander Adams towards a leadership role in accessibility, register her for the 'UX Design Fundamentals' course. Coordinate a mentorship session to occur 16 days from today. Adjust her mentorship focus areas to incorporate 'Advanced Accessibility Strategy'. Inform her with the message: 'Your pathway towards advanced accessibility leadership has been set. You are now enrolled in a new course, and a mentorship session is arranged.' Also, inform HR with the message: 'Alexander Adams's advanced accessibility leadership pathway is now established, including a new course enrollment and mentorship coordination.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getCourseIdByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "enrollInCourse",
                "arguments": {
                    "user_id": "U307",
                    "course_id": "C1002",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR003",
                    "session_date": "2025-10-18"
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR003",
                    "updates": {
                        "focus_areas": [
                            "Accessibility",
                            "Mentorship",
                            "Design Leadership",
                            "Advanced Accessibility Strategy"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U307",
                    "message": "Your advanced accessibility leadership pathway has been established. You have been enrolled in a new course and a mentorship session has been scheduled."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "An advanced accessibility leadership pathway has been established for Alexander Adams, including new course enrollment and mentorship coordination."
                }
            }
        ],
        "outputs": [
                "User U307 enrolled in course C1002",
                "\"scheduled_for\": \"2025-10-18\"",
                "relationship MR003 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_38",
        "instruction": "To prepare Robert Thompson for enterprise-level performance, arrange an executive coaching session to take place 10 days from now. Modify his mentorship focus areas to add 'Executive Coaching'. Communicate with him using the message: 'To aid your enterprise-level performance objectives, an executive coaching session has been arranged and your mentorship plan is updated.' Additionally, inform HR with the message: 'An executive coaching session has been organized for Robert Thompson to further his enterprise-level performance objectives.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR004",
                    "session_date": "2025-10-12"
                },
            },
            {
                "name": "updateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR004",
                    "updates": {
                        "focus_areas": [
                            "Site Reliability Engineering",
                            "Leadership",
                            "Infrastructure",
                            "Executive Coaching"
                        ],
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U306",
                    "message": "To support your enterprise-level performance goals, an executive coaching session has been scheduled and your mentorship plan has been updated."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "An executive coaching session has been scheduled for Robert Thompson to support his enterprise-level performance goals."
                }
            }
        ],
        "outputs": [
                "\"scheduled_for\": \"2025-10-12\"",
                "relationship MR004 updated",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_39",
        "instruction": "Enhance Robert Thompson' primary career development goal by advancing its progress to 50%. Additionally, arrange a mentorship session set for 12 days from today to monitor his progress. Inform him with the message: 'Your career advancement goal has been updated. A new mentorship session has been scheduled to track your progress.' and inform HR with the message: 'Robert Thompson' primary career goal has been advanced and a new mentorship session has been scheduled.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "listUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR004",
                    "session_date": "2025-10-14"
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "updates": {
                        "progress_percent": 50,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U306",
                    "message": "Your career advancement goal has been updated. A new mentorship session has been scheduled to track your progress."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "Robert Thompson' primary career goal has been advanced and a new mentorship session has been scheduled."
                }
            }
        ],
        "outputs": [
                "\"scheduled_for\": \"2025-10-14\"",
                "Goal G306-1 updated for user U306",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_40",
        "instruction": "To finalize David Adams's skill verification, increase his 'AWS Security' goal progress to 70%. Arrange a mentorship session for 20 days from today to verify certification readiness. Communicate to him with the message: 'Your skill validation is complete. Your goal progress has been updated, and a mentorship session has been scheduled to confirm certification readiness.' and communicate to HR with the message: 'A comprehensive skill validation for David Adams has been completed. His goal progress has been updated and a mentorship session is scheduled.'",
        "actions": [
            {
                "name": "getUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getGoalIdByDescription",
                "arguments": {
                    "user_id": "U303",
                    "keyword": "AWS Security"
                },
            },
            {
                "name": "listUserMentorships",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "getTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "updateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "updates": {
                        "progress_percent": 70,
                        "last_updated": "2025-10-02"
                    }
                },
            },
            {
                "name": "scheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR006",
                    "session_date": "2025-10-22"
                },
            },
            {
                "name": "notifyUser",
                "arguments": {
                    "user_id": "U303",
                    "message": "Your skill validation is complete. Your goal progress has been updated, and a mentorship session has been scheduled to confirm certification readiness."
                },
            },
            {
                "name": "notifyHr",
                "arguments": {
                    "message": "A comprehensive skill validation for David Adams has been completed. His goal progress has been updated and a mentorship session is scheduled."
                }
            }
        ],
        "outputs": [
                "Goal G303-1 updated for user U303",
                "\"scheduled_for\": \"2025-10-22\"",
                "notified_user",
                "\"notified\": \"HR\""
        ]
    }
]
