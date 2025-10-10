# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMortgageProfileTool(Tool):
    """Creates or updates a mortgage profile entry in the mortgage_profiles table."""

    @staticmethod
    def invoke(data: Dict[str, Any], annual_income, client_id, credit_score, down_payment, interest_rate, loan_amount, region, term_years) -> str:
        client_id = _as_int(client_id)
        term_years = _as_int(term_years)

        if (
            client_id is None
            or loan_amount is None
            or down_payment is None
            or interest_rate is None
            or term_years is None
        ):
            return _err(
                "client_id, loan_amount, down_payment, interest_rate, and term_years are required"
            )

        # Non-mandatory fields
        credit_score = _as_int(credit_score)

        # Allow for the misspelling "mortage_profiles."
        if "mortgage_profiles" in data:
            rows = data.setdefault("mortgage_profiles", [])
        else:
            rows = data.setdefault("mortage_profiles", [])

        existing = _get_mortgage_profile(data, client_id)
        if existing:
            # Modify the current profile.
            existing.update(
                {
                    "credit_score": credit_score,
                    "annual_income": annual_income,
                    "down_payment": float(down_payment),
                    "desired_loan_amount": float(loan_amount),
                    "interest_rate": float(interest_rate),
                    "term_years": term_years,
                    "region": region,
                    "last_reviewed_at": HARD_TS,
                }
            )
            return json.dumps(existing, indent=2)
        else:
            # Generate a new user profile.
            mortgage_id = _next_int_id(rows, "mortgage_id")
            rec = {
                "mortgage_id": mortgage_id,
                "client_id": client_id,
                "credit_score": credit_score,
                "annual_income": annual_income,
                "down_payment": float(down_payment),
                "desired_loan_amount": float(loan_amount),
                "interest_rate": float(interest_rate),
                "term_years": term_years,
                "region": region,
                "last_reviewed_at": HARD_TS,
            }
            rows.append(rec)
            return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_mortgage_profile",
                "description": (
                    "Creates a new mortgage profile for a client, or updates existing one."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "loan_amount": {"type": "number"},
                        "down_payment": {"type": "number"},
                        "interest_rate": {"type": "number"},
                        "term_years": {"type": "integer"},
                        "credit_score": {"type": ["integer", "null"]},
                        "annual_income": {"type": ["number", "null"]},
                        "region": {"type": ["string", "null"]},
                    },
                    "required": [
                        "client_id",
                        "loan_amount",
                        "down_payment",
                        "interest_rate",
                        "term_years",
                    ],
                },
            },
        }
