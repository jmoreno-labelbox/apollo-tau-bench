import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> Dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "benefit_plans.json")) as f:
        benefit_plans_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "compensation_records.json")) as f:
        compensation_records_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "departments.json")) as f:
        departments_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "employees.json")) as f:
        employees_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "performance_reviews.json")) as f:
        performance_reviews_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "positions.json")) as f:
        positions_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "ethnicity_codes.json")) as f:
        ethnicity_codes_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "job_levels.json")) as f:
        job_levels_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "leave_records.json")) as f:
        leave_records_data = json.load(f)
    return {
        "benefit_plans": benefit_plans_data,
        "compensation_records": compensation_records_data,
        "departments": departments_data,
        "employees": employees_data,
        "performance_reviews": performance_reviews_data,
        "positions": positions_data,
        "ethnicity_codes": ethnicity_codes_data,
        "job_levels": job_levels_data,
        "leave_records": leave_records_data
    }
