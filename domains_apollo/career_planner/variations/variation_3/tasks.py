# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "res_101",
        "instruction": "A succession plan that is thorough needs to be put in place for the role of Backend Tech Lead for Robert Thompson. Determine the best-qualified individual from the Engineering Team (T003).",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U306",
                        "U312"
                    ]
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U312",
                    "course_id": "C1004"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": [
                "Course assigned to user.",
                "Candidate shortlisted."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_102",
        "instruction": "Facilitate the career progression of Michael Rodriguez (U304) to DesignOps Lead by conducting a complete readiness evaluation and officially confirming his succession course.",
        "actions": [
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_103",
        "instruction": "Handle the creation of a successor promotion pipeline for the Clinical Analytics Lead position under the direction of Ava Nguyen, head of the Data Analytics Team (T001). This should include team analysis, recognition of leadership potential, and the preparation of qualified candidates.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T001"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U301",
                        "U302"
                    ]
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                }
            }
        ],
        "outputs": [
                "Course assigned to user.",
                "Candidate shortlisted."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_104",
        "instruction": "Coordinate the process of identifying potential leaders as the manager of the Product Design Team (T002). For Michael Rodriguez (U304), undertake a detailed readiness evaluation for the DesignOps Lead role, and if found suitable, officially place him on the succession shortlist.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T002"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U304",
                        "U307"
                    ]
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_105",
        "instruction": "Handle a thorough readiness evaluation for Alexander Adams in relation to the People Analytics Lead position, ensuring alignment of goals and identification of skill gaps. Attempt to allocate a verified course for her most critical skill gap. Finalize by officially recording her candidacy by placing her on the shortlist for the position.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Alexander Adams"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Statistical Modeling"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_106",
        "instruction": "Coordinate the placement of Michael Rodriguez (U304) for the DesignOps Lead position. Conduct a detailed appraisal of his goal alignment and skill deficiencies, then get him prepared for the position by assigning specific training and placing him on the succession shortlist.",
        "actions": [
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1004"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": [
                "Course assigned to user.",
                "Candidate shortlisted."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_107",
        "instruction": "Initiate a leadership development program for the Engineering Team (T003). Firstly, pinpoint all team members who have formal leadership objectives. For each of these individuals, conduct a thorough readiness evaluation for their intended position. Should training be necessary and an appropriate course is available, allocate it. Finalize by officially shortlisting each candidate for their intended role.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U306",
                        "U312"
                    ]
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_108",
        "instruction": "Initiate a skill enhancement program for the Data Analytics Team (T001). For each member (Ava Nguyen and Harper Bennett), determine their formal target role. If such a role is identified, carry out a detailed readiness evaluation and shortlist them. Should there be a need for training for any of their objectives and a suitable course is available, assign it.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Harper Bennett"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U302"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_109",
        "instruction": "Handle a readiness assessment for each member of the Engineering Team (T003). Should a member need training, propose and allocate a validated course to address their most critical skill gap.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_110",
        "instruction": "Coordinate a leadership development program for the Engineering Team (T003). Identify all team members with formal leadership objectives. Conduct a thorough readiness assessment for each of these candidates concerning their intended role. If training is necessary and a suitable course is available, allocate it. Conclude by officially shortlisting each candidate for their intended role.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U306",
                        "U312"
                    ]
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_111",
        "instruction": "Design a detailed development strategy for Ava Nguyen to advance to the position of Director of Data Science. The strategy should include validation of goal alignment, analysis of skill gaps, identification of training needs, assignment of an approved course, and formal consideration for the role.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_112",
        "instruction": "Develop a thorough readiness strategy for Michael Rodriguez (U304) to move into the DesignOps Lead role. Confirm his alignment, evaluate his gaps in technical and soft skills, provide appropriate training, and officially monitor his progression for the position.",
        "actions": [
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1004"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": [
                "Candidate shortlisted."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_113",
        "instruction": "Formulate a detailed development strategy for Ava Nguyen's promotion to Director of Data Science. This strategy should assess his preparedness, provide approved training for areas needing improvement, and officially list him as a candidate for the position.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_114",
        "instruction": "Organize a thorough DesignOps leadership growth plan for Michael Rodriguez. The plan should incorporate goal alignment confirmation, evaluation of skill deficiencies, and official succession planning.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_115",
        "instruction": "Coordinate a detailed readiness assessment for Michael Rodriguez for the Backend Tech Lead role by evaluating his objectives and examining his skill deficiencies. Following an attempt to identify an appropriate training course, finalize the procedure by formally documenting his development path through shortlisting.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_116",
        "instruction": "Conduct an in-depth readiness assessment for Emily Johnson's transition to UX Writer by checking his goal alignment and identifying skill gaps. Finish the process by formally solidifying his candidacy for the role through shortlisting.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Emily Johnson"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_117",
        "instruction": "Handle a thorough readiness evaluation for Alexander Adams's shift to People Analytics Lead by checking her goals and identifying any skill deficiencies. Seek out and confirm an appropriate training program. Wrap up the process by formally placing her on the shortlist for the position.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Alexander Adams"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Statistical Modeling"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_118",
        "instruction": "Coordinate a detailed data-science readiness sprint for the Analytics Team (T001). For each participant, assess their preparedness for their outlined target role, assign the highest-priority training, and create a succession plan for the team's management.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T001"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                }
            }
        ],
        "outputs": [
                "Course assigned to user.",
                "Candidate shortlisted."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_119",
        "instruction": "Formulate a detailed succession plan for the Engineering Team (T003). For the two members with leadership aspirations, Michael Rodriguez (U312) and Robert Thompson (U306), confirm their career objectives, assign the highest-priority training to address their skill deficiencies, and officially shortlist them for their intended target roles.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U306",
                        "U312"
                    ]
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_170",
        "instruction": "Get Ava Nguyen ready for the Director of Data Science role. Confirm his career objectives, evaluate his skill gaps, and assign a validated course to enhance his machine learning capabilities.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_171",
        "instruction": "Initiate a company-wide career transition program. For all employees with a 'Role Transition' goal (Ava Nguyen, Michael Rodriguez, Ava Nguyen, Robert Thompson, Emily Johnson, Alexander Adams, and Michael Rodriguez), first determine their formal target role alongside their current role. Next, conduct a thorough readiness assessment. If training is necessary and a suitable course is available, allocate it. Finish by formalizing each employee's transition plan through shortlisting them.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Robert Thompson"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Emily Johnson"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Alexander Adams"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U305"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U305"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1006",
                    "skill_name": "Product Marketing"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U308"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U308",
                    "target_role": "UX Writer"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U310"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U310"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Statistical Modeling"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_172",
        "instruction": "Evaluate Alexander Adams's suitability for the People Analytics Lead role. Conduct a detailed assessment of her development requirements, endeavor to assign approved training, and finalize by positioning her for succession from her current HR Partner role by shortlisting her.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Alexander Adams"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Statistical Modeling"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_173",
        "instruction": "Initiate a cross-functional leadership program. Assess the readiness of Robert Thompson from the Engineering team for the 'Staff SRE' position in comparison with Michael Rodriguez from the Product Design team for the 'DesignOps Lead' position. Conduct a detailed readiness assessment for each candidate and, provided they are found ready, proceed to formally establish their succession plan by shortlisting them.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Robert Thompson"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_174",
        "instruction": "Conduct a competitive leadership assessment for the Engineering Team (T003). Determine all members with leadership aspirations. For each individual, carry out a thorough readiness evaluation for their intended target role. If additional training is necessary and an appropriate course is available, assign it. Finalize by formally shortlisting each eligible candidate for their targeted role.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Robert Thompson"
                },
            },
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U306",
                        "U312"
                    ]
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_175",
        "instruction": "Assess Ava Nguyen's suitability for the Product Marketing Specialist position. Conduct a thorough evaluation of her developmental needs, try to allocate a validated training course, and finish by positioning her for advancement from her current Brand Strategist role by shortlisting her.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1006",
                    "skill_name": "Product Marketing"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_176",
        "instruction": "Coordinate a comparative assessment of leadership readiness for key candidates from the Product Design and Engineering teams. Evaluate Michael Rodriguez for his preparedness for the 'DesignOps Lead' role. Evaluate Michael Rodriguez for his preparedness for the 'Backend Tech Lead' role. If either candidate is ready, officially establish their succession path by shortlisting them. Should training be necessary but no valid course is available, continue with shortlisting.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_177",
        "instruction": "Coordinate a leadership readiness comparison for principal candidates from the Engineering and Product Design teams. For Robert Thompson, evaluate his readiness for the 'Staff SRE' role. For Michael Rodriguez, evaluate his readiness for the 'DesignOps Lead' role. For both, officially establish their succession pathway by shortlisting them.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Robert Thompson"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_178",
        "instruction": "Supervise a comparative career development evaluation for Harper Bennett and Michael Rodriguez. For each, confirm their leadership objectives. For Michael Rodriguez, evaluate his readiness for the Backend Tech Lead role, endeavor to confirm a training course for his skill deficiencies, and officially shortlist him for the position.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Harper Bennett"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U302"
                },
            },
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_179",
        "instruction": "To develop cross-functional leadership, pinpoint the most suitable candidates for the DesignOps Lead and People Analytics Lead positions from their respective teams (T002 and T008). Analyze their expertise, review their backgrounds, and register them for specific training programs.",
        "actions": [
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T002"
                },
            },
            {
                "name": "GetTeamMembers",
                "arguments": {
                    "team_id": "T008"
                },
            },
            {
                "name": "GetUsersWithLeadershipGoals",
                "arguments": {
                    "user_ids": [
                        "U304",
                        "U307",
                        "U310"
                    ]
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U310",
                    "target_role": "People Analytics Lead"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U304",
                    "course_id": "C1004"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U310",
                    "course_id": "C1005"
                }
            }
        ],
        "outputs": [
                "Course assigned to user.",
                "DesignOps Lead"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_190",
        "instruction": "Create a promotional trajectory for Ava Nguyen (U301) to ascend to Director of Data Science. Review his foundational skills, allocate the relevant specialization training, and officially monitor his progress.",
        "actions": [
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                }
            }
        ],
        "outputs": [
                "Course assigned to user."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_191",
        "instruction": "Handle a comparative career transition analysis for Ava Nguyen and Michael Rodriguez. For each individual, coordinate a thorough readiness assessment for their intended role (Product Marketing Specialist and Backend Tech Lead). If they require training but no suitable course is identified, proceed to officially chart their transition plan by placing them on the shortlist.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U305"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1006",
                    "skill_name": "Product Marketing"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_192",
        "instruction": "Assess Michael Rodriguez's (U312) suitability for the Backend Tech Lead role. Evaluate his technical competencies and developmental needs, then prepare him for succession by allocating focused training and placing him on the shortlist.",
        "actions": [
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1004",
                    "skill_name": "Team Leadership"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_193",
        "instruction": "Coordinate a leadership readiness comparison for prominent candidates from Product Design and Analytics: Michael Rodriguez for the 'DesignOps Lead' role and Ava Nguyen for the 'Director of Data Science' position. For each individual, execute a thorough assessment, allocate validated training if necessary, and formally determine their succession route by shortlisting them.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U304"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserTargetRole",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_194",
        "instruction": "Formulate a development plan for Ava Nguyen's progression to Director of Data Science. Evaluate his preparedness, designate validated training for his most critical skill gap, and formalize his professional trajectory by shortlisting him.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Ava Nguyen"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_195",
        "instruction": "Set up a promotion pathway for Ava Nguyen (U301) to become Director of Data Science. The plan must confirm his preparedness, allocate validated training for his most crucial skill gap, and officially shortlist him for the position.",
        "actions": [
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_196",
        "instruction": "Conduct a thorough readiness evaluation for Harper Bennett's (U302) move to Clinical Analytics Lead. Confirm her experience with the Data Analytics Team (T001), assess her developmental requirements, provide targeted training, and officially position her for succession.",
        "actions": [
            {
                "name": "ValidateTeamMembership",
                "arguments": {
                    "user_id": "U302",
                    "team_id": "T001"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead"
                }
            }
        ],
        "outputs": [
                "Course assigned to user.",
                "Candidate shortlisted."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_197",
        "instruction": "For Robert Thompson of the Engineering Team (T003), handle a thorough readiness assessment for the Staff SRE position. Make an effort to allocate approved training for his most critical skill gap. Finalize by officially identifying his succession pathway by shortlisting him.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Robert Thompson"
                },
            },
            {
                "name": "ValidateTeamMembership",
                "arguments": {
                    "user_id": "U306",
                    "team_id": "T003"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U306",
                    "target_role": "Staff SRE"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_198",
        "instruction": "Ava Nguyen (U301) must address his skill gaps for the Director of Data Science position. Coordinate a development plan that pinpoints his top-priority training requirement, confirms the recommended course, and assigns it to him.",
        "actions": [
            {
                "name": "GetUserGoals",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_199",
        "instruction": "For Michael Rodriguez of the Product Design Team (T002), handle a comprehensive readiness assessment for the DesignOps Lead role. If the assessment indicates that training is necessary, assign a suitable course. Conclude by formalizing his succession plan by shortlisting him.",
        "actions": [
            {
                "name": "GetUserId",
                "arguments": {
                    "user_name": "Michael Rodriguez"
                },
            },
            {
                "name": "ValidateTeamMembership",
                "arguments": {
                    "user_id": "U304",
                    "team_id": "T002"
                },
            },
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U304",
                    "target_role": "DesignOps Lead"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_230",
        "instruction": "Establish a promotion track for Ava Nguyen (U301) to Director of Data Science. Coordinate a thorough assessment of his foundational needs, assign advanced training, and formalize his succession plan.",
        "actions": [
            {
                "name": "ValidateUserGoalAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "GetUserSkillGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "AssessSoftSkillAlignment",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "CheckTrainingNeeded",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "RecommendCourseForGap",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                },
            },
            {
                "name": "ValidateCourseSkillMapping",
                "arguments": {
                    "course_id": "C1005",
                    "skill_name": "Machine Learning"
                },
            },
            {
                "name": "LogTeamTraining",
                "arguments": {
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005"
                },
            },
            {
                "name": "AssignCourseToUser",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005"
                },
            },
            {
                "name": "ShortlistSuccessorCandidate",
                "arguments": {
                    "user_id": "U301",
                    "target_role": "Director of Data Science"
                }
            }
        ],
        "outputs": []
    }
]
