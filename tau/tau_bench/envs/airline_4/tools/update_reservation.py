from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class UpdateReservation(Tool):
    """API tool for altering existing flight reservations for customers. Enables updates to flights, passengers, baggage, insurance, and other reservation details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        flights: list[dict[str, Any]] | None = None,
        passengers: list[dict[str, str]] | None = None,
        cabin: str | None = None,
        total_baggages: int | None = None,
        nonfree_baggages: int | None = None,
        insurance: str | None = None,
        payment_method_id: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that the necessary parameter is valid
        if not reservation_id:
            payload = {"error": "Missing required parameter", "required": "reservation_id"}
            out = json.dumps(
                payload)
            return out

        #Locate the reservation
        reservations = data.get("reservations", [])
        target_reservation = None
        reservation_index = None

        for i, reservation in enumerate(reservations):
            if reservation.get("reservation_id") == reservation_id:
                target_reservation = reservation
                reservation_index = i
                break

        if not target_reservation:
            payload = {"error": "Reservation not found", "reservation_id": reservation_id}
            out = json.dumps(
                payload)
            return out

        #Identify the user linked to this reservation
        user_id = target_reservation.get("user_id")
        users = data.get("users", [])
        target_user = None
        user_index = None

        for i, user in enumerate(users):
            user_reservations = user.get("reservations", [])
            if reservation_id in user_reservations:
                target_user = user
                user_index = i
                break

        if not target_user:
            payload = {
                    "error": "User not found for reservation",
                    "reservation_id": reservation_id,
                    "user_id": user_id,
                }
            out = json.dumps(
                payload)
            return out

        #Keep original values for potential rollback
        original_total_cost = sum(
            flight.get("price", 0) for flight in target_reservation.get("flights", [])
        )
        updates_made = []

        #Retain original cabin for calculating upgrade costs
        original_cabin = target_reservation.get("cabin")
        cabin_upgrade_cost = 0

        #Check and revise cabin class if supplied
        if cabin is not None:
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

            #Determine the cost of upgrading the cabin if a change is made
            if original_cabin and original_cabin != cabin:
                #Establish the pricing framework for cabin upgrades
                cabin_multipliers = {
                    "basic_economy": 1.0,
                    "economy": 1.2,
                    "business": 1.8,
                    "first": 2.5,
                }

                original_multiplier = cabin_multipliers.get(original_cabin, 1.0)
                new_multiplier = cabin_multipliers.get(cabin, 1.0)

                #Compute the upgrade cost based on flight prices and the difference in cabin
                base_cost = sum(
                    flight.get("price", 0)
                    for flight in target_reservation.get("flights", [])
                )
                cabin_upgrade_cost = base_cost * (new_multiplier - original_multiplier)

                #Verify that the upgrade cost is non-negative (refunds should apply for downgrades)
                if cabin_upgrade_cost < 0:
                    cabin_upgrade_cost = cabin_upgrade_cost  #Maintain negative values for refunds

            target_reservation["cabin"] = cabin
            updates_made.append("cabin")

        #Check and revise insurance if supplied
        if insurance is not None:
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
            target_reservation["insurance"] = insurance
            updates_made.append("insurance")

        #Check and revise baggage if supplied
        if total_baggages is not None:
            if not isinstance(total_baggages, int) or total_baggages < 0:
                payload = {
                        "error": "total_baggages must be a non-negative integer",
                        "received": total_baggages,
                    }
                out = json.dumps(
                    payload)
                return out
            target_reservation["total_baggages"] = total_baggages
            updates_made.append("total_baggages")

        if nonfree_baggages is not None:
            if not isinstance(nonfree_baggages, int) or nonfree_baggages < 0:
                payload = {
                        "error": "nonfree_baggages must be a non-negative integer",
                        "received": nonfree_baggages,
                    }
                out = json.dumps(
                    payload)
                return out
            target_reservation["nonfree_baggages"] = nonfree_baggages
            updates_made.append("nonfree_baggages")

        #Check and revise flights if supplied
        new_total_cost = original_total_cost
        if flights is not None:
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

            #Revise flights and compute the new total cost
            target_reservation["flights"] = flights
            new_total_cost = sum(flight["price"] for flight in flights)
            updates_made.append("flights")

            #Revise origin and destination according to new flights
            if flights:
                target_reservation["origin"] = flights[0]["origin"]
                target_reservation["destination"] = flights[-1]["destination"]
                updates_made.extend(["origin", "destination"])

        #Check and revise passengers if supplied
        if passengers is not None:
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

            target_reservation["passengers"] = passengers
            updates_made.append("passengers")

        #Manage payment adjustments if the cost has changed, cabin upgraded, or a new payment method is supplied
        cost_difference = new_total_cost - original_total_cost + cabin_upgrade_cost
        payment_processed = False

        if payment_method_id is not None or cost_difference != 0:
            #If a new payment method is supplied, confirm its existence
            if payment_method_id is not None:
                payment_methods = target_user.get("payment_methods", {})
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

                #For cost increases or a new payment method, ensure there are sufficient funds
                if cost_difference > 0 or payment_method_id is not None:
                    if payment_method["source"] in ["gift_card", "certificate"]:
                        available_amount = payment_method.get("amount", 0)
                        required_amount = (
                            cost_difference if cost_difference > 0 else new_total_cost
                        )

                        if available_amount < required_amount:
                            payload = {
                                    "error": "Insufficient funds in payment method",
                                    "payment_method_id": payment_method_id,
                                    "available_amount": available_amount,
                                    "required_amount": required_amount,
                                }
                            out = json.dumps(
                                payload)
                            return out

                #Handle the payment adjustment
                if cost_difference != 0:
                    #Include an entry in the payment history
                    if "payment_history" not in target_reservation:
                        target_reservation["payment_history"] = []

                    target_reservation["payment_history"].append(
                        {"payment_id": payment_method_id, "amount": cost_difference}
                    )

                    #Revise the balance of the payment method for gift cards and certificates
                    if payment_method["source"] in ["gift_card", "certificate"]:
                        if cost_difference > 0:  #Extra fee
                            new_amount = payment_method["amount"] - cost_difference
                            data["users"][user_index]["payment_methods"][
                                payment_method_id
                            ]["amount"] = new_amount
                        elif cost_difference < 0:  #Reimbursement
                            new_amount = payment_method["amount"] + abs(cost_difference)
                            data["users"][user_index]["payment_methods"][
                                payment_method_id
                            ]["amount"] = new_amount

                    payment_processed = True
                    updates_made.append("payment")

        #Revise the total cost of the reservation
        target_reservation["total_cost"] = new_total_cost + cabin_upgrade_cost

        #Revise the reservation within the database
        data["reservations"][reservation_index] = target_reservation

        #Compute the updated trip summary
        flights = target_reservation.get("flights", [])
        passengers = target_reservation.get("passengers", [])
        trip_summary = {
            "total_flights": len(flights),
            "total_cost": new_total_cost + cabin_upgrade_cost,
            "departure_date": flights[0].get("date") if flights else None,
            "return_date": flights[-1].get("date") if len(flights) > 1 else None,
            "passenger_count": len(passengers),
        }

        #Formulate response
        response = {
            "success": True,
            "message": "Reservation updated successfully",
            "reservation_id": reservation_id,
            "updates_made": updates_made,
            "trip_summary": trip_summary,
            "updated_reservation": target_reservation,
        }

        if payment_processed:
            response["payment_adjustment"] = {
                "cost_difference": cost_difference,
                "new_total_cost": new_total_cost + cabin_upgrade_cost,
                "original_total_cost": original_total_cost,
                "cabin_upgrade_cost": (
                    cabin_upgrade_cost if cabin_upgrade_cost != 0 else None
                ),
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservation",
                "description": "Modify existing flight reservations. Allows updating flights, passengers, cabin class, baggage, insurance, and payment methods. Automatically handles payment adjustments for cost changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier to update (e.g., '4WQ150', 'A7K2M9')",
                        },
                        "flights": {
                            "type": "array",
                            "description": "Updated flight segments. Each flight must include origin, destination, flight_number, date (YYYY-MM-DD), and price",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "origin": {"type": "string"},
                                    "destination": {"type": "string"},
                                    "flight_number": {"type": "string"},
                                    "date": {"type": "string"},
                                    "price": {"type": "number"},
                                },
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "description": "Updated passenger list. Each passenger must include first_name, last_name, and dob (YYYY-MM-DD)",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {"type": "string"},
                                },
                            },
                        },
                        "cabin": {
                            "type": "string",
                            "description": "Updated cabin class: 'basic_economy', 'economy', 'business', or 'first'",
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Updated total number of baggage items",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Updated number of paid baggage items",
                        },
                        "insurance": {
                            "type": "string",
                            "description": "Updated travel insurance option: 'yes' or 'no'",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "Payment method ID for processing cost differences (e.g., 'credit_card_4421486', 'gift_card_5309492')",
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }
