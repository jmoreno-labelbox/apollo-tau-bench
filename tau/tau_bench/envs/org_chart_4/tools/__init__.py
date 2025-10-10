# Copyright owned by Sierra

from .get_employee import get_employee
from .get_all_employees import get_all_employees
from .get_department import get_department
from .get_departments import get_departments
from .get_position import get_position
from .get_positions import get_positions
from .get_compensation_records import get_compensation_records
from .get_performance_reviews import get_performance_reviews
from .get_leave_records import get_leave_records
from .add_employee import add_employee
from .update_employee import update_employee
from .delete_employee import delete_employee
from .add_department import add_department
from .add_position import add_position
from .add_compensation_record import add_compensation_record
from .add_performance_review import add_performance_review
from .add_leave_record import add_leave_record

ALL_TOOLS = [
    get_employee,
    get_all_employees,
    get_department,
    get_departments,
    get_position,
    get_positions,
    get_compensation_records,
    get_performance_reviews,
    get_leave_records,
    add_employee,
    update_employee,
    delete_employee,
    add_department,
    add_position,
    add_compensation_record,
    add_performance_review,
    add_leave_record,
]
