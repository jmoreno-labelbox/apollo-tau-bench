# Copyright Sierra

from .search_tasks import SearchTasks
from .create_task import CreateTask
from .get_task_details import GetTaskDetails
from .update_task_status import UpdateTaskStatus
from .create_sprint import CreateSprint
from .mark_sprint_as_reviewed import MarkSprintAsReviewed
from .assign_task_to_sprint import AssignTaskToSprint
from .get_sprint_details import GetSprintDetails
from .calculate_sprint_burndown import CalculateSprintBurndown
from .reassign_task import ReassignTask
from .update_sprint_status import UpdateSprintStatus
from .get_team_velocity import GetTeamVelocity
from .create_task_dependency import CreateTaskDependency
from .get_backlog_tasks import GetBacklogTasks
from .log_time_on_task import LogTimeOnTask
from .escalate_task import EscalateTask
from .calculate_team_capacity import CalculateTeamCapacity
from .create_sprint_retrospective import CreateSprintRetrospective
from .get_task_history import GetTaskHistory
from .update_task_priority import UpdateTaskPriority
from .get_employee_workload import GetEmployeeWorkload
from .bulk_move_tasks_to_sprint import BulkMoveTasksToSprint
from .clone_task import CloneTask
from .resolve_blocked_task import ResolveBlockedTask
from .generate_sprint_report import GenerateSprintReport
from .check_blocked_tasks_for_escalation import CheckBlockedTasksForEscalation
from .check_time_logging_compliance import CheckTimeLoggingCompliance

ALL_TOOLS = [
    SearchTasks,
    CreateTask,
    GetTaskDetails,
    UpdateTaskStatus,
    CreateSprint,
    MarkSprintAsReviewed,
    AssignTaskToSprint,
    GetSprintDetails,
    CalculateSprintBurndown,
    ReassignTask,
    UpdateSprintStatus,
    GetTeamVelocity,
    CreateTaskDependency,
    GetBacklogTasks,
    LogTimeOnTask,
    EscalateTask,
    CalculateTeamCapacity,
    CreateSprintRetrospective,
    GetTaskHistory,
    UpdateTaskPriority,
    GetEmployeeWorkload,
    BulkMoveTasksToSprint,
    CloneTask,
    ResolveBlockedTask,
    GenerateSprintReport,
    CheckBlockedTasksForEscalation,
    CheckTimeLoggingCompliance,
]
