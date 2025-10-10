RULES = [
    "Before starting a sprint, always verify team capacity and ensure planned story points do not exceed 80% of the team's average velocity from the last 2 completed sprints. For new teams without velocity history, limit sprint capacity to 20 story points per team member.",
    "Tasks with unresolved dependencies cannot be moved to 'in_progress' status. Before updating any task status to 'in_progress', check all dependency tasks are in 'done' status. Tasks blocked by dependencies must have their blocked_by field updated.",
    "No individual team member should have more than 25 story points assigned in an active sprint. When assigning tasks, check the employee's current sprint workload and redistribute if this limit would be exceeded.",
    "Sprints must follow the status progression: planning -> active -> completed. Only one sprint per team can be in 'active' status at a time.",
    "Active sprints must have their burndown calculated daily. If completion percentage falls below expected linear progress by more than 20%, identify blocked tasks and consider re-planning or escalation.",
    "Critical priority tasks must be assigned to senior team members (proficiency level 4+) unless no senior members are available. Tasks cannot be reassigned more than twice per sprint without management approval.",
    "Every completed sprint must have a retrospective created within 2 days of completion. Retrospectives must include at least 1 item each for 'what went well', and  'what needs improvement'. Action items from retrospectives must be converted to tasks in the next sprint.",
    "All tasks in 'in_progress' or 'done' status must have time logged at least every 2 days. Tasks marked as 'done' must have a minimum of 50% of their estimated story points in logged hours (assuming 1 story point = 2 hours).",
    "Once a sprint moves to 'active' status, new tasks can only be added if: they are critical priority, OR, equivalent story points are removed, OR team velocity allows and all team members agree. All scope changes must be documented in task history."
]
