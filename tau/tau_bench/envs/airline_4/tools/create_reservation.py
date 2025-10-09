from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateReservation(Tool):
    """API tool for establishing new flight reservations for customers."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        user_id: str,
        user_email: str,
        origin: str,
        destination: str,
        flight_type: str,
        cabin: str,
        flights: list[dict[str, Any]],
        passengers: list[dict[str, str]],
        payment_method_id: str,
        created_at: str,
        total_baggages: int = 0,
        nonfree_baggages: int = 0,
        insurance: str = "no",
    ) -> str:
        pass
        #Check that necessary parameters are valid
        if not all(
            [
                reservation_id,
                user_id,
                user_email,
                origin,
                destination,
                flight_type,
                cabin,
                flights,
                passengers,
                payment_method_id,
                created_at,
            ]
        ):
            payload = {
                    "error": "Missing required parameters",
                    "required": [
                        "reservation_id",
                        "user_id",
                        "user_email",
                        "origin",
                        "destination",
                        "flight_type",
                        "cabin",
                        "flights",
                        "passengers",
                        "payment_method_id",
                        "created_at",
                    ],
                }
            out = json.dumps(
                payload)
            return out

        #Confirm the flight_type is valid
        valid_flight_types = ["one_way", "round_trip", "multi_city"]
        if flight_type not in valid_flight_types:
            payload = {
                    "error": "Invalid flight_type",
                    "valid_flight_types": valid_flight_types,
                    "received": flight_type,
                }
            out = json.dumps(
                payload)
            return out

        #Ensure the cabin class is valid
        valid_cabins = ["basic_economy", "economy", "business", "first"]
        if cabin not in valid_cabins:
            payload = {
                    "error": "Invalid cabin class",
                    "valid_cabins": valid_cabins,
                    "received": cabin,
                }
            out = json.dumps(
                payload)
            return out

        #Check that insurance is valid
        valid_insurance = ["yes", "no"]
        if insurance not in valid_insurance:
            payload = {
                    "error": "Invalid insurance option",
                    "valid_insurance": valid_insurance,
                    "received": insurance,
                }
            out = json.dumps(
                payload)
            return out

        #Locate user using their email
        users = data.get("users", {}).values()
        target_user = None
        user_index = None

        for i, user in enumerate(users.values()):
            if user.get("email") == user_email:
                target_user = user
                user_index = i
                break

        if not target_user:
            payload = {"error": "User not found", "email": user_email}
            out = json.dumps(payload)
            return out

        #Utilize the supplied user_id (should be deterministic)

        #Ensure the structure of flights is valid
        if not isinstance(flights, list) or len(flights) == 0:
            payload = {"error": "flights must be a non-empty array"}
            out = json.dumps(payload)
            return out

        for i, flight in enumerate(flights):
            required_flight_fields = [
                "origin",
                "destination",
                "flight_number",
                "date",
                "price",
            ]
            for field in required_flight_fields:
                if field not in flight:
                    payload = {
                            "error": f"Missing field '{field}' in flight {i+1}",
                            "required_flight_fields": required_flight_fields,
                        }
                    out = json.dumps(
                        payload)
                    return out

            #Check the date format for validity
            try:
                datetime.strptime(flight["date"], "%Y-%m-%d")
            except ValueError:
                payload = {
                        "error": f"Invalid date format in flight {i+1}. Expected YYYY-MM-DD",
                        "received": flight["date"],
                    }
                out = json.dumps(
                    payload)
                return out

            #Confirm that the price is numeric
            if not isinstance(flight["price"], (int, float)):
                payload = {
                        "error": f"Invalid price in flight {i+1}. Must be a number",
                        "received": flight["price"],
                    }
                out = json.dumps(
                    payload)
                return out

        #Ensure the structure of passengers is valid
        if not isinstance(passengers, list) or len(passengers) == 0:
            payload = {"error": "passengers must be a non-empty array"}
            out = json.dumps(payload)
            return out

        for i, passenger in enumerate(passengers):
            required_passenger_fields = ["first_name", "last_name", "dob"]
            for field in required_passenger_fields:
                if field not in passenger:
                    payload = {
                            "error": f"Missing field '{field}' in passenger {i+1}",
                            "required_passenger_fields": required_passenger_fields,
                        }
                    out = json.dumps(
                        payload)
                    return out

            #Check the format of the date of birth for validity
            try:
                datetime.strptime(passenger["dob"], "%Y-%m-%d")
            except ValueError:
                payload = {
                        "error": f"Invalid date of birth format for passenger {i+1}. Expected YYYY-MM-DD",
                        "received": passenger["dob"],
                    }
                out = json.dumps(
                    payload)
                return out

        #Confirm the existence of a payment method for the user
        payment_methods = target_user.get("payment_methods", {}).values()
        if payment_method_id not in payment_methods:
            available_methods = list(payment_methods.keys())
            payload = {
                    "error": "Payment method not found for user",
                    "payment_method_id": payment_method_id,
                    "available_payment_methods": available_methods,
                }
            out = json.dumps(
                payload)
            return out

        payment_method = payment_methods[payment_method_id]

        #Compute the total amount
        total_amount = sum(flight["price"] for flight in flights.values())

        #Ensure the payment method has adequate funds (for gift cards and certificates)
        if payment_method["source"] in ["gift_card", "certificate"]:
            available_amount = payment_method.get("amount", 0)
            if available_amount < total_amount:
                payload = {
                        "error": "Insufficient funds in payment method",
                        "payment_method_id": payment_method_id,
                        "available_amount": available_amount,
                        "required_amount": total_amount,
                    }
                out = json.dumps(
                    payload)
                return out

        #Confirm that the reservation ID is unique
        existing_reservations = data.get("reservations", {}).values()
        if any(
            res.get("reservation_id") == reservation_id for res in existing_reservations.values()
        ):
            payload = {
                    "error": "Reservation ID already exists",
                    "reservation_id": reservation_id,
                }
            out = json.dumps(
                payload)
            return out

        #Establish a reservation
        reservation = {
            "reservation_id": reservation_id,
            "user_id": user_id,
            "origin": origin,
            "destination": destination,
            "flight_type": flight_type,
            "cabin": cabin,
            "flights": flights,
            "passengers": passengers,
            "payment_history": [
                {"payment_id": payment_method_id, "amount": total_amount}
            ],
            "created_at": created_at,
            "total_baggages": total_baggages,
            "nonfree_baggages": nonfree_baggages,
            "insurance": insurance,
        }

        #Include the reservation in the database
        if "reservations" not in data:
            data["reservations"] = []
        data["reservations"][reservation_id] = reservation

        #Revise the user's list of reservations
        if "reservations" not in target_user:
            target_user["reservations"] = []
        target_user["reservations"].append(reservation_id)

        #Revise the balance of the payment method for gift cards and certificates
        if payment_method["source"] in ["gift_card", "certificate"]:
            new_amount = payment_method["amount"] - total_amount
            data["users"][user_index]["payment_methods"][payment_method_id][
                "amount"
            ] = new_amount

        #Formulate response
        response = {
            "success": True,
            "message": "Reservation created successfully",
            "reservation": reservation,
            "user": {
                "email": target_user.get("email"),
                "name": target_user.get("name"),
                "membership": target_user.get("membership"),
            },
            "payment_details": {
                "payment_method_id": payment_method_id,
                "payment_source": payment_method["source"],
                "amount_charged": total_amount,
            },
        }

        #Include the remaining balance for gift cards and certificates
        if payment_method["source"] in ["gift_card", "certificate"]:
            response["payment_details"]["remaining_balance"] = new_amount
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReservation",
                "description": "Create a new flight reservation for a customer. Validates user, flights, passengers, and payment method, then creates the reservation and updates user records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier (e.g., 'RSV001', '4WQ150'). Must be unique across all reservations.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., 'chen_jackson_3290'). Must match existing user.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "Customer email address to identify the user",
                        },
                        "origin": {
                            "type": "string",
                            "description": "Trip origin IATA code (e.g., 'DFW')",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Trip destination IATA code (e.g., 'LAX')",
                        },
                        "flight_type": {
                            "type": "string",
                            "description": "Type of trip. Must be one of: 'one_way', 'round_trip', 'multi_city'",
                        },
                        "cabin": {
                            "type": "string",
                            "description": "Cabin class. Must be one of: 'basic_economy', 'economy', 'business', 'first'",
                        },
                        "flights": {
                            "type": "array",
                            "description": "Array of flight segments",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "origin": {
                                        "type": "string",
                                        "description": "Flight segment origin IATA code",
                                    },
                                    "destination": {
                                        "type": "string",
                                        "description": "Flight segment destination IATA code",
                                    },
                                    "flight_number": {
                                        "type": "string",
                                        "description": "Flight number (e.g., 'HAT170')",
                                    },
                                    "date": {
                                        "type": "string",
                                        "description": "Flight date in YYYY-MM-DD format",
                                    },
                                    "price": {
                                        "type": "number",
                                        "description": "Flight segment price",
                                    },
                                },
                                "required": [
                                    "origin",
                                    "destination",
                                    "flight_number",
                                    "date",
                                    "price",
                                ],
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "description": "Array of passengers",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {
                                        "type": "string",
                                        "description": "Passenger first name",
                                    },
                                    "last_name": {
                                        "type": "string",
                                        "description": "Passenger last name",
                                    },
                                    "dob": {
                                        "type": "string",
                                        "description": "Passenger date of birth in YYYY-MM-DD format",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "Payment method ID from user's available payment methods",
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Total number of baggage items (default: 0)",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Number of paid baggage items (default: 0)",
                        },
                        "insurance": {
                            "type": "string",
                            "description": "Travel insurance option. Must be 'yes' or 'no' (default: 'no')",
                        },
                        "created_at": {
                            "type": "string",
                            "description": "Reservation creation timestamp in YYYY-MM-DDTHH:MM:SS format. Required for deterministic behavior.",
                        },
                    },
                    "required": [
                        "reservation_id",
                        "user_id",
                        "user_email",
                        "origin",
                        "destination",
                        "flight_type",
                        "cabin",
                        "flights",
                        "passengers",
                        "payment_method_id",
                        "created_at",
                    ],
                },
            },
        }
