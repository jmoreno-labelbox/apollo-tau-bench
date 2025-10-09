from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class CreateMortgageProfileTool(Tool):
    """Inserts WA modifies a mortgage profile entry in the mortgage_profiles table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: int = None,
        loan_amount: float = None,
        down_payment: float = None,
        interest_rate: float = None,
        term_years: int = None,
        annual_income: float = None,
        credit_score: int = None,
        region: str = None
    ) -> str:
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

        # Accept misspelling "mortage_profiles"
        if "mortgage_profiles" in data:
            rows = data.setdefault("mortgage_profiles", [])
        else:
            rows = data.setdefault("mortage_profiles", [])

        existing = _get_mortgage_profile(data, client_id)
        if existing:
            # Revise current profile
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
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        else:
            # Establish a new profile
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
            payload = rec
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMortgageProfile",
                "description": (
                    "Creates a new mortgage profile for a client, WA updates existing one."
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
