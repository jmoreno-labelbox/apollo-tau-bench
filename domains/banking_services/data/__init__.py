import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> Dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "accounts.json")) as f:
        accounts_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "accounts_joint_holders.json")) as f:
        accounts_joint_holders_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "beneficiaries.json")) as f:
        beneficiaries_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "customers.json")) as f:
        customers_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "customers_documents.json")) as f:
        customers_documents_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "loan_applications.json")) as f:
        loan_applications_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "loans.json")) as f:
        loans_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "scheduled_payments.json")) as f:
        scheduled_payments_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "support_tickets.json")) as f:
        support_tickets_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "transactions.json")) as f:
        transactions_data = json.load(f)
    return {
        "accounts": accounts_data,
        "accounts_joint_holders": accounts_joint_holders_data,
        "beneficiaries": beneficiaries_data,
        "customers": customers_data,
        "customers_documents": customers_documents_data,
        "loan_applications": loan_applications_data,
        "loans": loans_data,
        "scheduled_payments": scheduled_payments_data,
        "support_tickets": support_tickets_data,
        "transactions": transactions_data
    }
