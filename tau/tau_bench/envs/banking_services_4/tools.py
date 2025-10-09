import json
from datetime import datetime, timezone
from typing import Any, Dict, List
from tau_bench.envs.tool import Tool
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00.000000"

def generate_unique_id() -> str:
    return 'fd520c73'

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

class GetCustomerAccountsByType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_type: str = None) -> str:
        if not customer_id or not account_type:
            return json.dumps({'error': 'customer_id and account_type are required'})
        accounts = load_json('accounts.json')
        filtered = [a for a in accounts.values() if a['customer_id'] == customer_id and a['account_type'].lower() == account_type.lower()]
        return json.dumps(filtered, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getCustomerAccountsByType',
                'description': 'Returns a customer\'s accounts filtered by account type (e.g., "Savings").',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'account_type': {'type': 'string', 'description': 'Account type (e.g., Savings, Checking, Credit Card, etc.)'}
                    },
                    'required': ['customer_id', 'account_type']
                }
            }
        }

class ListRecentTransactionsByCategory(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        account_ids: list = None,
        group_by: str = 'merchant_name',
        limit: int = 10
    ) -> str:
        if not account_ids:
            return json.dumps({'error': 'account_ids is required'})
        transactions = load_json('transactions.json')
        filtered = [t for t in transactions.values() if t['account_id'] in account_ids]
        filtered.sort(key=lambda t: t['transaction_date'], reverse=True)
        filtered = filtered[:limit]
        grouped = {}
        for t in filtered:
            key = t.get(group_by) or 'Unknown'
            grouped.setdefault(key, []).append(t)
        return json.dumps(grouped, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'listRecentTransactionsByCategory',
                'description': 'Lists recent transactions grouped by merchant or spending category.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of account IDs'},
                        'group_by': {'type': 'string', 'description': 'Group by merchant_name or transaction_type', 'default': 'merchant_name'},
                        'limit': {'type': 'integer', 'description': 'Number of recent transactions to consider', 'default': 10}
                    },
                    'required': ['account_ids']
                }
            }
        }

class GetScheduledPaymentsDueInRange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], start_date: str = None, end_date: str = None) -> str:
        if not start_date or not end_date:
            return json.dumps({'error': 'start_date and end_date are required'})
        payments = load_json('scheduled_payments.json')
        results = []
        for p in payments:
            if p['status'] != 'Active':
                continue
            npd = p.get('next_payment_date')
            if npd and start_date <= npd <= end_date:
                results.append(p)
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getScheduledPaymentsDueInRange',
                'description': 'Returns all active scheduled payments that fall within a given date range.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'start_date': {'type': 'string', 'description': 'Start date (YYYY-MM-DD)'},
                        'end_date': {'type': 'string', 'description': 'End date (YYYY-MM-DD)'}
                    },
                    'required': ['start_date', 'end_date']
                }
            }
        }

class GetCustomerRiskProfileSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})
        customers = load_json('customers.json')
        customer = next((c for c in customers.values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({'error': 'Customer not found'})
        summary = {
            'aml_risk_level': customer.get('compliance', {}).values().get('aml_risk_level'),
            'credit_score': customer.get('financial_profile', {}).values().get('credit_score'),
            'kyc_status': customer.get('compliance', {}).values().get('kyc_status')
        }
        return json.dumps(summary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getCustomerRiskProfileSummary',
                'description': 'Retrieves AML risk level, credit score, and KYC status.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'}
                    },
                    'required': ['customer_id']
                }
            }
        }

class GetCustomerContactMethods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})
        customers = load_json('customers.json')
        customer = next((c for c in customers.values() if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({'error': 'Customer not found'})
        contact_info = customer.get('contact_info', {}).values()
        preferences = customer.get('preferences', {}).values()
        result = {
            'email_address': contact_info.get('email_address'),
            'phone_numbers': contact_info.get('phone_numbers'),
            'communication_channel': preferences.get('communication_channel')
        }
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getCustomerContactMethods',
                'description': 'Returns current contact preferences and phone/email on file.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'}
                    },
                    'required': ['customer_id']
                }
            }
        }

class ListActiveLoansWithBalances(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})
        loans = load_json('loans.json')
        filtered = [l for l in loans.values() if l['customer_id'] == customer_id and l['status'] == 'Active']
        result = [
            {
                'loan_id': l['loan_id'],
                'loan_type': l['loan_type'],
                'current_balance': l['current_balance'],
                'account_id': l['account_id']
            }
            for l in filtered
        ]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'listActiveLoansWithBalances',
                'description': 'Returns all active loans and their current outstanding balances.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'}
                    },
                    'required': ['customer_id']
                }
            }
        }

class FetchBeneficiariesByRelationship(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, relationship: str = None) -> str:
        if not customer_id or not relationship:
            return json.dumps({'error': 'customer_id and relationship are required'})
        beneficiaries = load_json('beneficiaries.json')
        filtered = [b for b in beneficiaries.values() if b['customer_id'] == customer_id and b['relationship'].lower() == relationship.lower()]
        return json.dumps(filtered, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'fetchBeneficiariesByRelationship',
                'description': 'Returns beneficiaries based on relationship type (e.g., "Friend", "Family").',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'relationship': {'type': 'string', 'description': 'Relationship type (e.g., Friend, Family, etc.)'}
                    },
                    'required': ['customer_id', 'relationship']
                }
            }
        }

class GetPaymentScheduleForAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        payments = load_json('scheduled_payments.json')
        filtered = [p for p in payments.values() if p['source_account_id'] == account_id]
        return json.dumps(filtered, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getPaymentScheduleForAccount',
                'description': 'Returns all recurring payment details for a specific account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }

class FindRecentSupportTicketsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, category: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})

        tickets = load_json('support_tickets.json')
        filtered = [t for t in tickets.values() if t['customer_id'] == customer_id]

        if category:
            filtered = [t for t in filtered.values() if t.get('category') == category]

        # Sort by created_at or updated_at if available for "recent"
        filtered.sort(key=lambda x: x.get('created_at', ''), reverse=True)

        return json.dumps(filtered, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'findRecentSupportTicketsByCategory',
                'description': 'Retrieves recent support tickets for a customer optionally filtered by category.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'category': {'type': 'string', 'description': 'Optional category filter'}
                    },
                    'required': ['customer_id']
                }
            }
        }


class GetTotalDepositsOverPeriod(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_ids: list = None, start_date: str = None, end_date: str = None) -> str:
        if not account_ids or not start_date or not end_date:
            return json.dumps({'error': 'account_ids, start_date, and end_date are required'})
        transactions = load_json('transactions.json')
        total = 0.0
        for t in transactions:
            if t['account_id'] in account_ids and t['transaction_type'] == 'Deposit':
                t_date = t['transaction_date'][:10]
                if start_date <= t_date <= end_date:
                    total += t['amount']
        return json.dumps({'total_deposits': total}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getTotalDepositsOverPeriod',
                'description': 'Sums all deposit-type transactions for a given date range.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of account IDs'},
                        'start_date': {'type': 'string', 'description': 'Start date (YYYY-MM-DD)'},
                        'end_date': {'type': 'string', 'description': 'End date (YYYY-MM-DD)'}
                    },
                    'required': ['account_ids', 'start_date', 'end_date']
                }
            }
        }

class VerifyBeneficiaryExists(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id: str = None) -> str:
        if not beneficiary_id:
            return json.dumps({'error': 'beneficiary_id is required'})
        beneficiaries = load_json('beneficiaries.json')
        beneficiary = next((b for b in beneficiaries.values() if b['beneficiary_id'] == beneficiary_id), None)
        if not beneficiary:
            return json.dumps({'error': 'Beneficiary not found.'})
        return json.dumps(beneficiary, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'verifyBeneficiaryExists',
                'description': 'Verifies a beneficiary exists by their ID and returns their details.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'beneficiary_id': {'type': 'string', 'description': 'Beneficiary ID to verify'}
                    },
                    'required': ['beneficiary_id']
                }
            }
        }

class ReassignRelationshipManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, relationship_manager_id: str = None) -> str:
        if not customer_id or not relationship_manager_id:
            return json.dumps({'error': 'customer_id and relationship_manager_id are required'})
        customers = load_json('customers.json')
        updated = False
        for c in customers:
            if c['customer_id'] == customer_id:
                if 'bank_relationship' not in c or 'relationship_manager_id' not in c['bank_relationship']:
                    return json.dumps({'error': 'Relationship manager reassignment not supported: no relationship_manager_id field in data.'})
                c['bank_relationship']['relationship_manager_id'] = relationship_manager_id
                updated = True
        if not updated:
            return json.dumps({'error': 'Customer not found or reassignment not supported.'})
        return json.dumps({'success': True, 'customer_id': customer_id, 'relationship_manager_id': relationship_manager_id})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'reassignRelationshipManager',
                'description': 'Updates the assigned relationship manager for a customer (only if field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'relationship_manager_id': {'type': 'string', 'description': 'New Relationship Manager ID'}
                    },
                    'required': ['customer_id', 'relationship_manager_id']
                }
            }
        }

class DeactivateAccountByRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        updated = False
        for a in accounts:
            if a['account_id'] == account_id:
                if 'status' not in a:
                    return json.dumps({'error': 'Account deactivation not supported: no status field in data.'})
                a['status'] = 'Inactive'
                updated = True
        if not updated:
            return json.dumps({'error': 'Account not found or deactivation not supported.'})
        return json.dumps({'success': True, 'account_id': account_id, 'new_status': 'Inactive'})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'deactivateAccountByRequest',
                'description': 'Sets account status to "Inactive" for the specified account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }

class CreateSupportTicketForTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, transaction_id: str = None, reason: str = None) -> str:
        if not customer_id or not transaction_id or not reason:
            return json.dumps({'error': 'customer_id, transaction_id, and reason are required'})

        # This function would ideally append to the support_tickets.json file,
        # but here we just simulate the creation for demonstration.
        new_ticket = {
            "ticket_id": f"tkt_{generate_unique_id()}",
            "customer_id": customer_id,
            "status": "Open",
            "priority": "High",
            "channel": "System",
            "category": "Transaction Inquiry",
            "request_details": {
                "target_entity": "Transaction",
                "target_id": transaction_id,
                "operation": "INVESTIGATE",
                "parameters": { "reason": reason }
            }
        }
        return json.dumps({'success': True, 'ticket_created': new_ticket}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'createSupportTicketForTransaction',
                'description': 'Creates a high-priority support ticket to investigate a transaction.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'The ID of the customer reporting the issue.'},
                        'transaction_id': {'type': 'string', 'description': 'The ID of the transaction to be investigated.'},
                        'reason': {'type': 'string', 'description': 'The reason for creating the support ticket.'}
                    },
                    'required': ['customer_id', 'transaction_id', 'reason']
                }
            }
        }

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'createSupportTicketForTransaction',
                'description': 'Creates a high-priority support ticket to investigate a transaction.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'The ID of the customer reporting the issue.'
                        },
                        'transaction_id': {
                            'type': 'string',
                            'description': 'The ID of the transaction to be investigated.'
                        },
                        'reason': {
                            'type': 'string',
                            'description': 'The reason for creating the support ticket.'
                        }
                    },
                    'required': ['customer_id', 'transaction_id', 'reason']
                }
            }
        }

class UpdateScheduledPaymentAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None, amount: float = None) -> str:
        if not payment_id or amount is None:
            return json.dumps({'error': 'payment_id and amount are required'})
        payments = load_json('scheduled_payments.json')
        updated = False
        for p in payments:
            if p['payment_id'] == payment_id:
                if 'amount' not in p:
                    return json.dumps({'error': 'Scheduled payment update not supported: no amount field in data.'})
                p['amount'] = amount
                updated = True
        if not updated:
            return json.dumps({'error': 'Scheduled payment not found or update not supported.'})
        return json.dumps({'success': True, 'payment_id': payment_id, 'amount': amount})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'updateScheduledPaymentAmount',
                'description': 'Modifies the amount of a scheduled payment by ID (only if amount field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'payment_id': {'type': 'string', 'description': 'Scheduled Payment ID'},
                        'amount': {'type': 'number', 'description': 'New payment amount'}
                    },
                    'required': ['payment_id', 'amount']
                }
            }
        }

class MergeDuplicateCustomersBySSN(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ssn_last_4: str = None) -> str:
        if not ssn_last_4:
            return json.dumps({'error': 'ssn_last_4 is required'})
        customers = load_json('customers.json')
        matches = [c for c in customers.values() if c.get('personal_info', {}).values().get('ssn_last_4') == ssn_last_4]
        if len(matches) < 2:
            return json.dumps({'error': 'Less than two customers with this SSN'})
        # Only merge if all fields to be merged exist
        for c in matches:
            if 'account_ids' not in c:
                return json.dumps({'error': 'Customer merge not supported: account_ids field missing in one or more records.'})
        canonical = matches[0]
        merged_ids = [c['customer_id'] for c in matches[1:]]
        for c in matches[1:]:
            canonical['account_ids'] = list(set(canonical.get('account_ids', []) + c.get('account_ids', [])))
            customers.remove(c)
        return json.dumps({'success': True, 'canonical_customer_id': canonical['customer_id'], 'merged_customer_ids': merged_ids})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'mergeDuplicateCustomersBySsn',
                'description': 'Merges two customer records with same SSN into a single canonical one (only if account_ids field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'ssn_last_4': {'type': 'string', 'description': 'Last 4 digits of SSN'}
                    },
                    'required': ['ssn_last_4']
                }
            }
        }

class AddEmployerToCustomerProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, employer: str = None) -> str:
        if not customer_id or not employer:
            return json.dumps({'error': 'customer_id and employer are required'})
        customers = load_json('customers.json')
        updated = False
        for c in customers:
            if c['customer_id'] == customer_id:
                if 'personal_info' not in c or 'employer' not in c['personal_info']:
                    return json.dumps({'error': 'Employer update not supported: employer field missing in data.'})
                c['personal_info']['employer'] = employer
                updated = True
        if not updated:
            return json.dumps({'error': 'Customer not found or employer update not supported.'})
        return json.dumps({'success': True, 'customer_id': customer_id, 'employer': employer})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'addEmployerToCustomerProfile',
                'description': 'Updates the employer field for an existing customer (only if employer field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'},
                        'employer': {'type': 'string', 'description': 'Employer name'}
                    },
                    'required': ['customer_id', 'employer']
                }
            }
        }

class GetAccountOverdraftLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        account = next((a for a in accounts.values() if a['account_id'] == account_id), None)
        if not account:
            return json.dumps({'error': 'Account not found.'})
        if account.get('account_type') != 'Checking':
            return json.dumps({'error': 'Overdraft limit is only applicable to Checking accounts.'})

        limit = account.get('overdraft_limit')
        if limit is None:
            return json.dumps({'error': 'Overdraft limit field not found for this account.'})

        return json.dumps({'account_id': account_id, 'overdraft_limit': limit}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getAccountOverdraftLimit',
                'description': 'Retrieves the current overdraft limit for a specified checking account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'The ID of the checking account.'}
                    },
                    'required': ['account_id']
                }
            }
        }

class CloseActiveAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        updated = False
        for a in accounts:
            if a['account_id'] == account_id and a.get('status') == 'Active':
                if 'status' not in a:
                    return json.dumps({'error': 'Account closure not supported: no status field in data.'})
                a['status'] = 'Inactive'
                updated = True
        if not updated:
            return json.dumps({'error': 'Account not found or not eligible for closure.'})
        return json.dumps({'success': True, 'account_id': account_id})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'closeActiveAccount',
                'description': 'Sets an active account status to inactive (only if status field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }

class CheckFundsForNextScheduledPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None) -> str:
        if not payment_id:
            return json.dumps({'error': 'payment_id is required'})

        payments = load_json('scheduled_payments.json')
        payment = next((p for p in payments.values() if p['payment_id'] == payment_id), None)
        if not payment:
            return json.dumps({'error': 'Scheduled payment not found.'})

        accounts = load_json('accounts.json')
        source_account = next((a for a in accounts.values() if a['account_id'] == payment['source_account_id']), None)
        if not source_account:
            return json.dumps({'error': 'Source account for payment not found.'})

        payment_amount = payment['amount']
        account_balance = source_account['balance']
        sufficient_funds = account_balance >= payment_amount

        return json.dumps({
            'payment_id': payment_id,
            'next_payment_date': payment.get('next_payment_date'),
            'payment_amount': payment_amount,
            'account_balance': account_balance,
            'sufficient_funds': sufficient_funds
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'checkFundsForNextScheduledPayment',
                'description': 'Checks if the source account has enough funds for the next scheduled payment.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'payment_id': {'type': 'string', 'description': 'The ID of the scheduled payment to check.'}
                    },
                    'required': ['payment_id']
                }
            }
        }

class InitiateFundTransferToBeneficiary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_account_id: str = None, beneficiary_id: str = None, amount: float = None, description: str = None) -> str:
        if not source_account_id or not beneficiary_id or amount is None:
            return json.dumps({'error': 'source_account_id, beneficiary_id, and amount are required'})
        accounts = load_json('accounts.json')
        beneficiaries = load_json('beneficiaries.json')
        transactions = load_json('transactions.json')
        # Find source account
        src = next((a for a in accounts.values() if a['account_id'] == source_account_id and a['status'] == 'Active'), None)
        if not src or 'balance' not in src:
            return json.dumps({'error': 'Source account not found or not active, or missing balance field.'})
        # Find beneficiary
        bene = next((b for b in beneficiaries.values() if b['beneficiary_id'] == beneficiary_id), None)
        if not bene or 'account_details' not in bene:
            return json.dumps({'error': 'Beneficiary not found or missing account_details.'})
        if src['balance'] < amount:
            return json.dumps({'error': 'Insufficient funds.'})
        src['balance'] -= amount
        txn = {
            'transaction_id': f'txn_{generate_unique_id()}',
            'account_id': source_account_id,
            'transaction_date': get_current_timestamp(),
            'amount': -amount,
            'currency': src['currency'],
            'transaction_type': 'Transfer',
            'description': f'Transfer to beneficiary {bene["beneficiary_name"]}',
            'merchant_name': None,
            'status': 'Completed',
            'channel': 'Online'
        }
        data["transactions"][transaction_id] = txn
        return json.dumps({'success': True, 'transaction': txn})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'initiateFundTransferToBeneficiary',
                'description': 'Starts a one-time transfer to a saved beneficiary from a given account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'source_account_id': {'type': 'string', 'description': 'Source Account ID'},
                        'beneficiary_id': {'type': 'string', 'description': 'Beneficiary ID'},
                        'amount': {'type': 'number', 'description': 'Transfer amount'}
                    },
                    'required': ['source_account_id', 'beneficiary_id', 'amount']
                }
            }
        }

class MakeLoanOverpayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, from_account_id: str = None, amount: float = None) -> str:
        if not loan_id or not from_account_id or amount is None:
            return json.dumps({'error': 'loan_id, from_account_id, and amount are required'})
        loans = load_json('loans.json')
        accounts = load_json('accounts.json')
        transactions = load_json('transactions.json')
        loan = next((l for l in loans.values() if l['loan_id'] == loan_id), None)
        acct = next((a for a in accounts.values() if a['account_id'] == from_account_id and a['status'] == 'Active'), None)
        if not loan or 'current_balance' not in loan:
            return json.dumps({'error': 'Loan not found or missing current_balance.'})
        if not acct or 'balance' not in acct:
            return json.dumps({'error': 'Account not found or missing balance.'})
        if acct['balance'] < amount:
            return json.dumps({'error': 'Insufficient funds.'})
        acct['balance'] -= amount
        loan['current_balance'] = max(0, loan['current_balance'] - amount)
        txn = {
            'transaction_id': f'txn_{generate_unique_id()}',
            'account_id': from_account_id,
            'transaction_date': get_current_timestamp(),
            'amount': -amount,
            'currency': acct['currency'],
            'transaction_type': 'Loan Overpayment',
            'description': f'Overpayment to loan {loan_id}',
            'merchant_name': None,
            'status': 'Completed',
            'channel': 'Online'
        }
        data["transactions"][transaction_id] = txn
        return json.dumps({'success': True, 'transaction': txn, 'loan_id': loan_id, 'new_balance': loan['current_balance']})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'makeLoanOverpayment',
                'description': 'Applies an additional payment to a loan outside the regular schedule.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'loan_id': {'type': 'string', 'description': 'Loan ID'},
                        'from_account_id': {'type': 'string', 'description': 'Account to debit'},
                        'amount': {'type': 'number', 'description': 'Overpayment amount'}
                    },
                    'required': ['loan_id', 'from_account_id', 'amount']
                }
            }
        }

class AdjustLoanPaymentDueDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, new_due_date: str = None) -> str:
        if not loan_id or not new_due_date:
            return json.dumps({'error': 'loan_id and new_due_date are required'})
        loans = load_json('loans.json')
        loan = next((l for l in loans.values() if l['loan_id'] == loan_id), None)
        if not loan or 'maturity_date' not in loan:
            return json.dumps({'error': 'Loan not found or maturity_date not present.'})
        loan['maturity_date'] = new_due_date
        return json.dumps({'success': True, 'loan_id': loan_id, 'new_due_date': new_due_date})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'adjustLoanPaymentDueDate',
                'description': 'Modifies the due date of a loan repayment (policy-checked, only if maturity_date exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'loan_id': {'type': 'string', 'description': 'Loan ID'},
                        'new_due_date': {'type': 'string', 'description': 'New due date (YYYY-MM-DD)'}
                    },
                    'required': ['loan_id', 'new_due_date']
                }
            }
        }

class ApplyPartialRefundToTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str = None, refund_amount: float = None) -> str:
        if not transaction_id or refund_amount is None:
            return json.dumps({'error': 'transaction_id and refund_amount are required'})
        transactions = load_json('transactions.json')
        accounts = load_json('accounts.json')
        txn = next((t for t in transactions.values() if t['transaction_id'] == transaction_id), None)
        if not txn or 'account_id' not in txn or 'amount' not in txn or 'status' not in txn:
            return json.dumps({'error': 'Transaction not found or missing required fields.'})
        if txn['status'] != 'Completed' or txn['amount'] >= 0:
            return json.dumps({'error': 'Refund only allowed for completed debit transactions.'})
        acct = next((a for a in accounts.values() if a['account_id'] == txn['account_id'] and 'balance' in a), None)
        if not acct:
            return json.dumps({'error': 'Account not found or missing balance.'})
        if abs(refund_amount) > abs(txn['amount']):
            return json.dumps({'error': 'Refund amount exceeds original transaction.'})
        acct['balance'] += refund_amount
        refund_txn = {
            'transaction_id': f'txn_{generate_unique_id()}',
            'account_id': txn['account_id'],
            'transaction_date': get_current_timestamp(),
            'amount': refund_amount,
            'currency': acct['currency'],
            'transaction_type': 'Refund',
            'description': f'Partial refund for {transaction_id}',
            'merchant_name': None,
            'status': 'Completed',
            'channel': 'Online'
        }
        data["transactions"][transaction_id] = refund_txn
        return json.dumps({'success': True, 'refund_transaction': refund_txn})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'applyPartialRefundToTransaction',
                'description': 'Issues a partial refund to the account for a completed transaction.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'transaction_id': {'type': 'string', 'description': 'Original Transaction ID'},
                        'refund_amount': {'type': 'number', 'description': 'Refund amount'}
                    },
                    'required': ['transaction_id', 'refund_amount']
                }
            }
        }

class SplitTransactionBetweenAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str = None, splits: list = None) -> str:
        if not transaction_id or not splits or not isinstance(splits, list):
            return json.dumps({'error': 'transaction_id and splits (list of {account_id, amount}) are required'})
        transactions = load_json('transactions.json')
        accounts = load_json('accounts.json')
        orig_txn = next((t for t in transactions.values() if t['transaction_id'] == transaction_id), None)
        if not orig_txn or 'amount' not in orig_txn or 'account_id' not in orig_txn:
            return json.dumps({'error': 'Original transaction not found or missing fields.'})
        if abs(sum(s['amount'] for s in splits)) != abs(orig_txn['amount']):
            return json.dumps({'error': 'Split amounts must sum to original transaction amount.'})
        # Remove original transaction (simulate split)
        transactions.remove(orig_txn)
        new_txns = []
        for s in splits:
            acct = next((a for a in accounts.values() if a['account_id'] == s['account_id'] and 'balance' in a), None)
            if not acct:
                return json.dumps({'error': f'Account {s["account_id"]} not found or missing balance.'})
            acct['balance'] += s['amount']
            new_txn = {
                'transaction_id': f'txn_{generate_unique_id()}',
                'account_id': s['account_id'],
                'transaction_date': get_current_timestamp(),
                'amount': s['amount'],
                'currency': acct['currency'],
                'transaction_type': 'Split',
                'description': f'Split from {transaction_id}',
                'merchant_name': orig_txn.get('merchant_name'),
                'status': 'Completed',
                'channel': 'Online'
            }
            new_txns.append(new_txn)
            data["transactions"][transaction_id] = new_txn
        return json.dumps({'success': True, 'split_transactions': new_txns})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'splitTransactionBetweenAccounts',
                'description': 'Splits a charge across two or more linked accounts.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'transaction_id': {'type': 'string', 'description': 'Original Transaction ID'},
                        'splits': {'type': 'array', 'items': {'type': 'object'}, 'description': 'List of {account_id, amount}'}
                    },
                    'required': ['transaction_id', 'splits']
                }
            }
        }

class GetCustomerTotalBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})

        accounts = load_json('accounts.json')
        customer_accounts = [a for a in accounts.values() if a['customer_id'] == customer_id]

        if not customer_accounts:
            return json.dumps({'error': 'No accounts found for this customer.'})

        total_balance = sum(a.get('balance', 0) for a in customer_accounts.values()

        return json.dumps({
            'customer_id': customer_id,
            'total_balance': total_balance,
            'account_count': len(customer_accounts)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getCustomerTotalBalance',
                'description': 'Calculates the total balance of a customer across all their accounts.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'The ID of the customer.'}
                    },
                    'required': ['customer_id']
                }
            }
        }

class EnforceKYCRefreshForCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})

        customers = load_json('customers.json')
        updated = False

        for c in customers:
            if c['customer_id'] == customer_id:
                # Ensure 'compliance' dict exists
                compliance = c.setdefault('compliance', {}).values()
                # Always set 'kyc_status' to 'Refresh Required'
                compliance['kyc_status'] = 'Refresh Required'
                updated = True
                break

        if not updated:
            return json.dumps({'error': 'Customer not found or KYC enforcement not supported.'})

        return json.dumps({
            'success': True,
            'customer_id': customer_id,
            'new_kyc_status': 'Refresh Required'
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'enforceKycRefreshForCustomer',
                'description': 'Sets kyc_status to "Refresh Required" for a given customer.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'Customer ID'
                        }
                    },
                    'required': ['customer_id']
                }
            }
        }

class LockAccountManually(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        account = next((a for a in accounts.values() if a['account_id'] == account_id), None)
        if not account or 'status' not in account:
            return json.dumps({'error': 'Account not found or missing status field.'})
        if account['status'] == 'Locked':
            return json.dumps({'success': False, 'account_id': account_id, 'locked': True, 'note': 'Account is already locked.'})
        account['status'] = 'Locked'
        return json.dumps({'success': True, 'account_id': account_id, 'locked': True})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'lockAccountManually',
                'description': 'Manually locks an account by setting its status to "Locked".',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }

class ReviewOverdraftActivityAndAdjustLimit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, new_limit: int = None) -> str:
        if not account_id or new_limit is None:
            return json.dumps({'error': 'account_id and new_limit are required'})
        accounts = load_json('accounts.json')
        account = next((a for a in accounts.values() if a['account_id'] == account_id and a['account_type'] == 'Checking'), None)
        if not account or 'overdraft_limit' not in account:
            return json.dumps({'error': 'Account not found or overdraft_limit field missing.'})
        account['overdraft_limit'] = new_limit
        return json.dumps({'success': True, 'account_id': account_id, 'new_overdraft_limit': new_limit})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'reviewOverdraftActivityAndAdjustLimit',
                'description': 'Adjusts overdraft limit based on recent usage and account behavior (only if overdraft_limit field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Checking Account ID'},
                        'new_limit': {'type': 'number', 'description': 'New overdraft limit'}
                    },
                    'required': ['account_id', 'new_limit']
                }
            }
        }

class UpdateCustomerCommunicationPreference(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, new_channel: str = None) -> str:
        if not customer_id or not new_channel:
            return json.dumps({'error': 'customer_id and new_channel are required'})

        customers = load_json('customers.json')
        customer = next((c for c in customers.values() if c['customer_id'] == customer_id), None)

        if not customer:
            return json.dumps({'error': 'Customer not found.'})

        preferences = customer.get('preferences', {}).values()
        if 'communication_channel' not in preferences:
            return json.dumps({'error': 'Communication channel preference not found for this customer.'})

        preferences['communication_channel'] = new_channel

        return json.dumps({'success': True, 'customer_id': customer_id, 'new_communication_channel': new_channel})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'updateCustomerCommunicationPreference',
                'description': 'Updates the preferred communication channel for a customer.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'The ID of the customer to update.'},
                        'new_channel': {'type': 'string', 'description': 'The new preferred channel (e.g., Email, Phone, SMS).'}
                    },
                    'required': ['customer_id', 'new_channel']
                }
            }
        }

class CloseActiveAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})
        accounts = load_json('accounts.json')
        updated = False
        for a in accounts:
            if a['account_id'] == account_id and a.get('status') == 'Active':
                if 'status' not in a:
                    return json.dumps({'error': 'Account closure not supported: no status field in data.'})
                a['status'] = 'Inactive'
                updated = True
        if not updated:
            return json.dumps({'error': 'Account not found or not eligible for closure.'})
        return json.dumps({'success': True, 'account_id': account_id})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'closeActiveAccount',
                'description': 'Sets an active account status to inactive (only if status field exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {'type': 'string', 'description': 'Account ID'}
                    },
                    'required': ['account_id']
                }
            }
        }

class GetAllAccountsForCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required"})

        accounts = load_json("accounts.json")
        customer_accounts = [
            account for account in accounts.values() if account.get("customer_id") == customer_id
        ]

        return json.dumps({
            "customer_id": customer_id,
            "accounts": [
                {
                    "account_id": acct.get("account_id"),
                    "account_type": acct.get("account_type"),
                    "currency": acct.get("currency"),
                    "balance": acct.get("balance")
                }
                for acct in customer_accounts
            ]
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getAllAccountsForCustomer',
                'description': 'Retrieves all accounts (with type, currency, and balance) associated with a given customer ID.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'The ID of the customer whose accounts should be fetched.'
                        }
                    },
                    'required': ['customer_id']
                }
            }
        }

class CreateSupportTicketForAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_id: str = None, reason: str = None) -> str:
        if not customer_id or not account_id or not reason:
            return json.dumps({'error': 'customer_id, account_id, and reason are required'})

        new_ticket = {
            "ticket_id": f"tkt_{generate_unique_id()}",
            "customer_id": customer_id,
            "status": "Open",
            "priority": "High",
            "channel": "System",
            "category": "Account Inquiry",
            "request_details": {
                "target_entity": "Account",
                "target_id": account_id,
                "operation": "INVESTIGATE",
                "parameters": {"reason": reason}
            }
        }

        return json.dumps({'success': True, 'ticket_created': new_ticket}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'createSupportTicketForAccount',
                'description': 'Creates a high-priority support ticket to investigate an issue related to an account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'The ID of the customer reporting the issue.'
                        },
                        'account_id': {
                            'type': 'string',
                            'description': 'The ID of the account to be investigated.'
                        },
                        'reason': {
                            'type': 'string',
                            'description': 'The reason for creating the support ticket.'
                        }
                    },
                    'required': ['customer_id', 'account_id', 'reason']
                }
            }
        }

class GetAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({'error': 'account_id is required'})

        accounts = load_json('accounts.json')
        account = next((a for a in accounts.values() if a['account_id'] == account_id), None)

        if not account or 'balance' not in account or 'currency' not in account:
            return json.dumps({'error': 'Account not found or missing balance/currency field.'})

        return json.dumps({
            'account_id': account_id,
            'balance': account['balance'],
            'currency': account['currency']
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getAccountBalance',
                'description': 'Fetches the current balance and currency of a given account ID.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_id': {
                            'type': 'string',
                            'description': 'The ID of the account whose balance is requested.'
                        }
                    },
                    'required': ['account_id']
                }
            }
        }


class GetLoanDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None) -> str:
        if not loan_id:
            return json.dumps({"error": "loan_id is required"})

        loans = load_json("loans.json")

        loan = next((l for l in loans.values() if l["loan_id"] == loan_id), None)
        if not loan:
            return json.dumps({"error": f"Loan with ID '{loan_id}' not found"})

        return json.dumps({"loan_details": loan})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLoanDetails",
                "description": "Fetches detailed information for a specific loan using its loan_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_id": {
                            "type": "string",
                            "description": "The unique identifier of the loan."
                        }
                    },
                    "required": ["loan_id"]
                }
            }
        }

class ApplyTransactionAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, amount: float = None, reason: str = None) -> str:
        if account_id is None or amount is None or reason is None:
            return json.dumps({"error": "account_id, amount, and reason are required"})

        accounts = load_json("accounts.json")
        for account in accounts:
            if account["account_id"] == account_id:
                account["balance"] += amount

                return json.dumps({
                    "success": True,
                    "account_id": account_id,
                    "adjusted_amount": amount,
                    "new_balance": account["balance"],
                    "reason": reason
                })

        return json.dumps({
            "success": False,
            "error": f"Account with ID {account_id} not found."
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyTransactionAdjustment",
                "description": "Applies a manual credit or debit adjustment to a specified account, typically for dispute resolutions or corrections.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "The ID of the account to apply the adjustment to."
                        },
                        "amount": {
                            "type": "number",
                            "description": "The amount to adjust. Positive for credit, negative for debit."
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the adjustment (e.g., 'Dispute credit reversal')."
                        }
                    },
                    "required": ["account_id", "amount", "reason"]
                }
            }
        }
class TransferFundsBetweenAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], from_account_id: str = None, to_account_id: str = None, amount: float = None, reason: str = "Fund transfer") -> str:
        if not from_account_id or not to_account_id or amount is None:
            return json.dumps({"error": "from_account_id, to_account_id, and amount are required"})

        accounts = load_json("accounts.json")

        from_account = next((acc for acc in accounts.values() if acc["account_id"] == from_account_id), None)
        to_account = next((acc for acc in accounts.values() if acc["account_id"] == to_account_id), None)

        if from_account is None:
            return json.dumps({"error": f"from_account_id {from_account_id} not found"})
        if to_account is None:
            return json.dumps({"error": f"to_account_id {to_account_id} not found"})
        if from_account["balance"] < amount:
            return json.dumps({"error": "Insufficient funds in source account"})

        from_account["balance"] -= amount
        to_account["balance"] += amount

        return json.dumps({
            "success": True,
            "from_account_id": from_account_id,
            "to_account_id": to_account_id,
            "transferred_amount": amount,
            "reason": reason,
            "from_account_balance": from_account["balance"],
            "to_account_balance": to_account["balance"],
            "note": "Changes are in-memory only; not persisted to file."
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferFundsBetweenAccounts",
                "description": "Transfers a specified amount from one account to another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account_id": {
                            "type": "string",
                            "description": "The source account ID to debit funds from."
                        },
                        "to_account_id": {
                            "type": "string",
                            "description": "The destination account ID to credit funds to."
                        },
                        "amount": {
                            "type": "number",
                            "description": "The amount to transfer."
                        },
                        "reason": {
                            "type": "string",
                            "description": "Optional reason for the transfer."
                        }
                    },
                    "required": ["from_account_id", "to_account_id", "amount"]
                }
            }
        }



TOOLS = [
    GetCustomerAccountsByType(),
    ListRecentTransactionsByCategory(),
    GetScheduledPaymentsDueInRange(),
    GetCustomerRiskProfileSummary(),
    GetCustomerContactMethods(),
    ListActiveLoansWithBalances(),
    FetchBeneficiariesByRelationship(),
    GetPaymentScheduleForAccount(),
    FindRecentSupportTicketsByCategory(),
    GetTotalDepositsOverPeriod(),
    VerifyBeneficiaryExists(),
    ReassignRelationshipManager(),
    DeactivateAccountByRequest(),
    CreateSupportTicketForTransaction(),
    UpdateScheduledPaymentAmount(),
    MergeDuplicateCustomersBySSN(),
    AddEmployerToCustomerProfile(),
    GetAccountOverdraftLimit(),
    CheckFundsForNextScheduledPayment(),
    InitiateFundTransferToBeneficiary(),
    MakeLoanOverpayment(),
    AdjustLoanPaymentDueDate(),
    ApplyPartialRefundToTransaction(),
    SplitTransactionBetweenAccounts(),
    GetCustomerTotalBalance(),
    EnforceKYCRefreshForCustomer(),
    LockAccountManually(),
    ReviewOverdraftActivityAndAdjustLimit(),
    UpdateCustomerCommunicationPreference(),
    CloseActiveAccount(),
    GetAllAccountsForCustomer(),
    CreateSupportTicketForAccount(),
    GetAccountBalance(),
    GetLoanDetails(),
    ApplyTransactionAdjustment(),
    TransferFundsBetweenAccounts(),
]
