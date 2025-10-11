# Copyright Sierra

from .get_employee_profile import get_employee_profile
from .create_employee_from_offer_letter import create_employee_from_offer_letter
from .list_department_headcount import list_department_headcount
from .update_employee_compensation import update_employee_compensation
from .get_performance_review_status import get_performance_review_status
from .submit_performance_review import submit_performance_review
from .get_leave_calendar import get_leave_calendar
from .request_leave import request_leave
from .get_benefits_enrollment import get_benefits_enrollment
from .enroll_in_benefit import enroll_in_benefit
from .remove_from_benefit import remove_from_benefit
from .get_document_compliance_status import get_document_compliance_status
from .upload_employee_document import upload_employee_document
from .get_org_diversity_metrics import get_org_diversity_metrics
from .update_employee_job_level import update_employee_job_level
from .get_open_positions import get_open_positions
from .close_position import close_position
from .update_company_document_content import update_company_document_content
from .get_compensation_records import get_compensation_records
from .update_employee_status import update_employee_status

ALL_TOOLS = [
    get_employee_profile,
    create_employee_from_offer_letter,
    list_department_headcount,
    update_employee_compensation,
    get_performance_review_status,
    submit_performance_review,
    get_leave_calendar,
    request_leave,
    get_benefits_enrollment,
    enroll_in_benefit,
    remove_from_benefit,
    get_document_compliance_status,
    upload_employee_document,
    get_org_diversity_metrics,
    update_employee_job_level,
    get_open_positions,
    close_position,
    update_company_document_content,
    get_compensation_records,
    update_employee_status,
]
