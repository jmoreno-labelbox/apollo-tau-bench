# Sierra Copyright

from .search_employees import SearchEmployees
from .get_employee_allocations import GetEmployeeAllocations
from .get_project_details import GetProjectDetails
from .update_allocation import UpdateAllocation
from .calculate_employee_utilization import CalculateEmployeeUtilization
from .update_utilization_log import UpdateUtilizationLog
from .update_employees_utilization import UpdateEmployeesUtilization
from .search_projects import SearchProjects
from .calculate_employee_availability import CalculateEmployeeAvailability
from .create_resource_request import CreateResourceRequest
from .create_allocation import CreateAllocation
from .update_request_status import UpdateRequestStatus
from .update_department_capacity import UpdateDepartmentCapacity
from .get_department_capacity import GetDepartmentCapacity
from .get_team_details import GetTeamDetails
from .update_project_status import UpdateProjectStatus
from .update_project_required_hours import UpdateProjectRequiredHours
from .get_project_allocations import GetProjectAllocations
from .get_employee_details import GetEmployeeDetails
from .delete_allocation import DeleteAllocation
from .search_allocations import SearchAllocations
from .create_bench_assignment import CreateBenchAssignment
from .update_employee_status import UpdateEmployeeStatus
from .update_employees_department import UpdateEmployeesDepartment
from .update_teams_department import UpdateTeamsDepartment
from .check_allocation_duration import CheckAllocationDuration
from .create_rotation_schedule import CreateRotationSchedule
from .get_department_teams import GetDepartmentTeams
from .get_team_utilization import GetTeamUtilization
from .calculate_department_utilization import CalculateDepartmentUtilization
from .create_team import CreateTeam
from .create_project import CreateProject
from .create_department import CreateDepartment
from .update_departments_utilization import UpdateDepartmentsUtilization
from .delete_department import DeleteDepartment
from .get_department_details import GetDepartmentDetails
from .analyze_allocation_efficiency import AnalyzeAllocationEfficiency
from .consolidate_allocations import ConsolidateAllocations
from .reassign_junior_work import ReassignJuniorWork
from .calculate_optimization_metrics import CalculateOptimizationMetrics
from .create_resource_conflict import CreateResourceConflict
from .compare_project_priorities import CompareProjectPriorities
from .summarize_workload_rebalance import SummarizeWorkloadRebalance
from .summarize_reallocation import SummarizeReallocation
from .summarize_optimization_results import SummarizeOptimizationResults
from .summarize_team_expansion import SummarizeTeamExpansion
from .summarize_project_consolidation import SummarizeProjectConsolidation
from .validate_compliance_status import ValidateComplianceStatus
from .summarize_department_merger import SummarizeDepartmentMerger
from .summarize_project_phase_metrics import SummarizeProjectPhaseMetrics
from .summarize_hybrid_work_allocation import SummarizeHybridWorkAllocation

ALL_TOOLS = [
    SearchEmployees,
    GetEmployeeAllocations,
    GetProjectDetails,
    UpdateAllocation,
    CalculateEmployeeUtilization,
    UpdateUtilizationLog,
    UpdateEmployeesUtilization,
    SearchProjects,
    CalculateEmployeeAvailability,
    CreateResourceRequest,
    CreateAllocation,
    UpdateRequestStatus,
    UpdateDepartmentCapacity,
    GetDepartmentCapacity,
    GetTeamDetails,
    UpdateProjectStatus,
    UpdateProjectRequiredHours,
    GetProjectAllocations,
    GetEmployeeDetails,
    DeleteAllocation,
    SearchAllocations,
    CreateBenchAssignment,
    UpdateEmployeeStatus,
    UpdateEmployeesDepartment,
    UpdateTeamsDepartment,
    CheckAllocationDuration,
    CreateRotationSchedule,
    GetDepartmentTeams,
    GetTeamUtilization,
    CalculateDepartmentUtilization,
    CreateTeam,
    CreateProject,
    CreateDepartment,
    UpdateDepartmentsUtilization,
    DeleteDepartment,
    GetDepartmentDetails,
    AnalyzeAllocationEfficiency,
    ConsolidateAllocations,
    ReassignJuniorWork,
    CalculateOptimizationMetrics,
    CreateResourceConflict,
    CompareProjectPriorities,
    SummarizeWorkloadRebalance,
    SummarizeReallocation,
    SummarizeOptimizationResults,
    SummarizeTeamExpansion,
    SummarizeProjectConsolidation,
    ValidateComplianceStatus,
    SummarizeDepartmentMerger,
    SummarizeProjectPhaseMetrics,
    SummarizeHybridWorkAllocation,
]
