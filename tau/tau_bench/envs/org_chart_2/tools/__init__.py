# Copyright owned by Sierra

from .get_employee import get_employee
from .search_employees import search_employees
from .create_employee import create_employee
from .update_employee import update_employee
from .terminate_employee import terminate_employee
from .get_department import get_department
from .list_departments import list_departments
from .update_department import update_department
from .get_compensation import get_compensation
from .set_compensation import set_compensation
from .add_performance_review import add_performance_review
from .list_performance_reviews import list_performance_reviews
from .request_leave import request_leave
from .update_leave_status import update_leave_status
from .list_employee_leaves import list_employee_leaves
from .add_benefit_plan import add_benefit_plan
from .update_benefit_plan import update_benefit_plan
from .set_employee_benefits import set_employee_benefits
from .get_unused_employee_id import get_unused_employee_id
from .search_positions import search_positions
from .add_leave_record import add_leave_record
from .list_leave_records import list_leave_records
from .update_leave_record import update_leave_record
from .add_employee_document import add_employee_document
from .list_employee_documents import list_employee_documents
from .add_bonus_payment import add_bonus_payment
from .list_bonus_payments import list_bonus_payments
from .add_employee_benefits_conditionally import add_employee_benefits_conditionally
from .increase_employee_compensation import increase_employee_compensation
from .conditional_compensation_check_and_update import conditional_compensation_check_and_update
from .get_unused_document_id import get_unused_document_id
from .get_unused_review_id import get_unused_review_id
from .list_compensations import list_compensations
from .get_unused_leave_id import get_unused_leave_id
from .get_unused_compensation_id import get_unused_compensation_id
from .get_unused_bonus_id import get_unused_bonus_id

ALL_TOOLS = [
    get_employee,
    search_employees,
    create_employee,
    update_employee,
    terminate_employee,
    get_department,
    list_departments,
    update_department,
    get_compensation,
    set_compensation,
    add_performance_review,
    list_performance_reviews,
    request_leave,
    update_leave_status,
    list_employee_leaves,
    add_benefit_plan,
    update_benefit_plan,
    set_employee_benefits,
    get_unused_employee_id,
    search_positions,
    add_leave_record,
    list_leave_records,
    update_leave_record,
    add_employee_document,
    list_employee_documents,
    add_bonus_payment,
    list_bonus_payments,
    add_employee_benefits_conditionally,
    increase_employee_compensation,
    conditional_compensation_check_and_update,
    get_unused_document_id,
    get_unused_review_id,
    list_compensations,
    get_unused_leave_id,
    get_unused_compensation_id,
    get_unused_bonus_id,
]
