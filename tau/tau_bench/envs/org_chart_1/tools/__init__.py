# Copyright owned by Sierra

from .get_employee_by_id import get_employee_by_id
from .find_employees import find_employees
from .create_new_employee import create_new_employee
from .update_employee_record import update_employee_record
from .terminate_employee import terminate_employee
from .get_department_by_id import get_department_by_id
from .list_departments import list_departments
from .update_department_record import update_department_record
from .get_compensation_by_employee_id import get_compensation_by_employee_id
from .set_compensation import set_compensation
from .create_performance_review import create_performance_review
from .get_performance_reviews_by_employee_id import get_performance_reviews_by_employee_id
from .create_leave_record import create_leave_record
from .update_leave_status import update_leave_status
from .list_employee_leaves import list_employee_leaves
from .create_benefit_plan import create_benefit_plan
from .update_benefit_plan import update_benefit_plan
from .set_employee_benefits import set_employee_benefits
from .get_new_employee_id import get_new_employee_id
from .search_positions import search_positions
from .get_new_compensation_id import get_new_compensation_id
from .get_new_review_id import get_new_review_id
from .get_employee_by_ids_by_region import get_employee_by_ids_by_region
from .get_new_leave_id import get_new_leave_id

ALL_TOOLS = [
    get_employee_by_id,
    find_employees,
    create_new_employee,
    update_employee_record,
    terminate_employee,
    get_department_by_id,
    list_departments,
    update_department_record,
    get_compensation_by_employee_id,
    set_compensation,
    create_performance_review,
    get_performance_reviews_by_employee_id,
    create_leave_record,
    update_leave_status,
    list_employee_leaves,
    create_benefit_plan,
    update_benefit_plan,
    set_employee_benefits,
    get_new_employee_id,
    search_positions,
    get_new_compensation_id,
    get_new_review_id,
    get_employee_by_ids_by_region,
    get_new_leave_id,
]
