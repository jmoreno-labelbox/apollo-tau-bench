# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReservation(Tool):
    """
    API tool to modify existing flight reservations for customers.
    Allows updating flights, passengers, baggage, insurance, and other reservation details.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        reservation_id: str = None,
        flights: list = None,
        passengers: list = None,
        cabin: str = None,
        total_baggages: int = None,
        nonfree_baggages: int = None,
        insurance: bool = None,
        payment_method_id: str = None
    ) -> str:
        from datetime import datetime
        from typing import Optional, List
        import hashlib
        
        def generate_deterministic_timestamp(reservation_id: str, flight_date: str = None) -> str:
            """Generate deterministic timestamp based on reservation_id and flight_date"""
            # Use reservation_id as base, add flight_date if available
            base_string = reservation_id
            if flight_date:
                base_string += f"_{flight_date}"
            
            # Create hash to generate consistent timestamp components
            hash_obj = hashlib.md5(base_string.encode())
            hash_hex = hash_obj.hexdigest()
            
            # Use hash to generate deterministic but realistic timestamp
            # Based on flight date or current date range
            if flight_date:
                base_date = datetime.strptime(flight_date, "%Y-%m-%d")
            else:
                # Default to May 2024 (typical flight period)
                base_date = datetime(2024, 5, 15)
            
            # Add hours/minutes/seconds from hash for consistency
            hours = int(hash_hex[:2], 16) % 24
            minutes = int(hash_hex[2:4], 16) % 60
            seconds = int(hash_hex[4:6], 16) % 60
            
            deterministic_time = base_date.replace(hour=hours, minute=minutes, second=seconds)
            return deterministic_time.isoformat()

        if not reservation_id:
            return json.dumps({
                "status": "missing_parameter",
                "required": "reservation_id"
            })

        reservations = list(data.get("reservations", {}).values())
        target_reservation = None
        reservation_index = None

        for i, reservation in enumerate(reservations):
            if reservation.get("reservation_id") == reservation_id:
                target_reservation = reservation
                reservation_index = i
                break

        if not target_reservation:
            return json.dumps({
                "status": "not_found",
                "reservation_id": reservation_id
            })

        # Find the user associated with this reservation
        user_id = target_reservation.get("user_id")
        users = list(data.get("users", {}).values())
        target_user = None
        user_index = None

        for i, user in enumerate(users):
            user_reservations = user.get("reservations", [])
            if reservation_id in user_reservations:
                target_user = user
                user_index = i
                break

        if not target_user:
            return json.dumps({
                "status": "user_not_found",
                "reservation_id": reservation_id,
                "user_id": user_id
            })

        # Store original values for rollback if needed
        original_total_cost = sum(flight.get("price", 0) for flight in target_reservation.get("flights", []))
        updates_made = []

        # Store original cabin for upgrade cost calculation
        original_cabin = target_reservation.get("cabin")
        cabin_upgrade_cost = 0

        # Validate and update cabin class if provided
        if cabin is not None:
            valid_cabins = ["basic_economy", "economy", "business", "first"]
            if cabin not in valid_cabins:
                return json.dumps({
                    "status": "invalid_cabin",
                    "valid_cabins": valid_cabins,
                    "received": cabin
                })

            if original_cabin and original_cabin != cabin:
                # Cabin multipliers for pricing - these constants should be used consistently across all tasks
                # basic_economy: 1.0 (baseline), economy: 1.2 (+20%), business: 1.8 (+80%), first: 2.5 (+150%)
                cabin_multipliers = {
                    "basic_economy": 1.0,
                    "economy": 1.2,
                    "business": 1.8,
                    "first": 2.5
                }

                original_multiplier = cabin_multipliers.get(original_cabin, 1.0)
                new_multiplier = cabin_multipliers.get(cabin, 1.0)

                # Calculate upgrade cost based on flight prices and cabin difference
                base_cost = sum(flight.get("price", 0) for flight in target_reservation.get("flights", []))
                cabin_upgrade_cost = base_cost * (new_multiplier - original_multiplier)

                if cabin_upgrade_cost < 0:
                    cabin_upgrade_cost = 0  

            target_reservation["cabin"] = cabin
            updates_made.append("cabin")

        if insurance is not None:
            valid_insurance = ["yes", "no"]
            if insurance not in valid_insurance:
                return json.dumps({
                    "status": "invalid_insurance",
                    "valid_insurance": valid_insurance,
                    "received": insurance
                })
            target_reservation["insurance"] = insurance
            updates_made.append("insurance")

        if payment_method_id is not None:
            target_reservation["payment_method_id"] = payment_method_id
            updates_made.append("payment_method_id")

        if total_baggages is not None:
            if not isinstance(total_baggages, int) or total_baggages < 0:
                return json.dumps({
                    "status": "invalid_baggage",
                    "message": "total_baggages must be a non-negative integer",
                    "received": total_baggages
                })
            target_reservation["total_baggages"] = total_baggages
            updates_made.append("total_baggages")

        if nonfree_baggages is not None:
            if not isinstance(nonfree_baggages, int) or nonfree_baggages < 0:
                return json.dumps({
                    "status": "invalid_baggage",
                    "message": "nonfree_baggages must be a non-negative integer",
                    "received": nonfree_baggages
                })
            target_reservation["nonfree_baggages"] = nonfree_baggages
            updates_made.append("nonfree_baggages")

        new_total_cost = original_total_cost
        if flights is not None:
            if not isinstance(flights, list) or len(flights) == 0:
                return json.dumps({
                    "status": "invalid_flights",
                    "message": "flights must be a non-empty array"
                })

            for i, flight in enumerate(flights):
                required_flight_fields = ["origin", "destination", "flight_number", "date", "price"]
                for field in required_flight_fields:
                    if field not in flight:
                        return json.dumps({
                            "status": "missing_field",
                            "message": f"Missing field '{field}' in flight {i+1}",
                            "required_flight_fields": required_flight_fields
                        })

                try:
                    datetime.strptime(flight["date"], "%Y-%m-%d")
                except ValueError:
                    return json.dumps({
                        "status": "invalid_date",
                        "message": f"Invalid date format in flight {i+1}. Expected YYYY-MM-DD",
                        "received": flight["date"]
                    })

                if not isinstance(flight["price"], (int, float)):
                    return json.dumps({
                        "status": "invalid_price",
                        "message": f"Flight {i+1} has an invalid price '{flight['price']}'. Price must be a number.",
                        "received": flight["price"]
                    })

            target_reservation["flights"] = flights
            new_total_cost = sum(flight["price"] for flight in flights)
            updates_made.append("flights")

            if flights:
                target_reservation["origin"] = flights[0]["origin"]
                target_reservation["destination"] = flights[-1]["destination"]
                updates_made.extend(["origin", "destination"])

        if passengers is not None:
            if not isinstance(passengers, list) or len(passengers) == 0:
                return json.dumps({
                    "status": "invalid_passengers",
                    "message": "Passengers parameter must be a non-empty array containing passenger information."
                })

            for i, passenger in enumerate(passengers):
                required_passenger_fields = ["first_name", "last_name", "dob"]
                for field in required_passenger_fields:
                    if field not in passenger:
                        return json.dumps({
                            "status": "missing_field",
                            "message": f"Passenger {i+1} is missing the required field '{field}'. All passengers must include first_name, last_name, and dob.",
                            "required_passenger_fields": required_passenger_fields
                        })

                try:
                    datetime.strptime(passenger["dob"], "%Y-%m-%d")
                except ValueError:
                    return json.dumps({
                        "status": "invalid_dob",
                        "message": f"Passenger {i+1} has an invalid date of birth format '{passenger['dob']}'. Please use YYYY-MM-DD format.",
                        "received": passenger["dob"]
                    })

            target_reservation["passengers"] = passengers
            updates_made.append("passengers")

        cost_difference = new_total_cost - original_total_cost + cabin_upgrade_cost
        payment_processed = False

        if payment_method_id is not None or cost_difference != 0:
            # Initialize payment_method variable
            payment_method = None
            
            if payment_method_id is not None:
                payment_methods = target_user.get("payment_methods", {})
                if payment_method_id not in payment_methods:
                    available_methods = sorted([key for key in payment_methods])
                    # Try to find a payment method with sufficient funds
                    suitable_payment_method = None
                    if cost_difference > 0:
                        # For additional charges, prioritize credit cards and then gift cards with sufficient funds
                        for method_id in sorted(available_methods):
                            method = payment_methods[method_id]
                            if method["source"] == "credit_card":
                                suitable_payment_method = method_id
                                break
                            elif method["source"] in ["gift_card", "certificate"]:
                                if method.get("amount", 0) >= cost_difference:
                                    suitable_payment_method = method_id
                                    break
                    else:
                        # For refunds or no cost change, any payment method is fine
                        suitable_payment_method = available_methods[0] if available_methods else None
                    
                    if suitable_payment_method:
                        # Store the originally requested payment method before changing it
                        originally_requested = payment_method_id
                        payment_method_id = suitable_payment_method
                        # Set payment_method for the auto-selected method
                        payment_method = payment_methods[suitable_payment_method]
                        # Add a note about the automatic selection
                        if "payment_method_auto_selected" not in target_reservation:
                            target_reservation["payment_method_auto_selected"] = []
                        # Get flight date for deterministic timestamp
                        flight_date = target_reservation.get("flights", [{}])[0].get("date") if target_reservation.get("flights") else None
                        target_reservation["payment_method_auto_selected"].append({
                            "original_requested": originally_requested,
                            "auto_selected": suitable_payment_method,
                            "timestamp": generate_deterministic_timestamp(reservation_id, flight_date)
                        })
                    else:
                        # No suitable payment method found
                        if cost_difference > 0:
                            return json.dumps({
                                "status": "no_suitable_payment",
                                "message": f"No payment method has sufficient funds for the ${cost_difference} cost difference. Available payment methods: {available_methods}",
                                "cost_difference": cost_difference,
                                "available_payment_methods": available_methods
                            })
                        else:
                            return json.dumps({
                                "status": "no_payment_methods",
                                "message": "The user has no payment methods available for processing the reservation update."
                            })
                else:
                    # Payment method exists, check if it has sufficient funds
                    payment_method = payment_methods[payment_method_id]
                    if cost_difference > 0 and payment_method["source"] in ["gift_card", "certificate"]:
                        available_amount = payment_method.get("amount", 0)
                        if available_amount < cost_difference:
                            # Try to find another payment method with sufficient funds
                            alternative_methods = []
                            for method_id in sorted([key for key in payment_methods]):
                                method = payment_methods[method_id]
                                if method_id != payment_method_id:
                                    if method["source"] == "credit_card":
                                        alternative_methods.append(f"{method_id} (credit card)")
                                    elif method["source"] in ["gift_card", "certificate"]:
                                        if method.get("amount", 0) >= cost_difference:
                                            alternative_methods.append(f"{method_id} (${method.get('amount', 0)} available)")
                            
                            # If we have alternative methods, try to use one automatically
                            if alternative_methods:
                                # Try credit cards first, then gift cards with sufficient funds
                                original_payment_method_id = payment_method_id
                                for alt_method_id in sorted([key for key in payment_methods]):
                                    alt_method = payment_methods[alt_method_id]
                                    if alt_method_id != original_payment_method_id:
                                        if alt_method["source"] == "credit_card":
                                            # Switch to credit card
                                            payment_method_id = alt_method_id
                                            payment_method = alt_method
                                            # Add a note about the automatic switch
                                            if "payment_method_auto_switched" not in target_reservation:
                                                target_reservation["payment_method_auto_switched"] = []
                                            # Get flight date for deterministic timestamp
                                            flight_date = target_reservation.get("flights", [{}])[0].get("date") if target_reservation.get("flights") else None
                                            target_reservation["payment_method_auto_switched"].append({
                                                "original_method": original_payment_method_id,
                                                "switched_to": alt_method_id,
                                                "reason": "insufficient_funds",
                                                "timestamp": generate_deterministic_timestamp(reservation_id, flight_date)
                                            })
                                            break
                                        elif alt_method["source"] in ["gift_card", "certificate"]:
                                            if alt_method.get("amount", 0) >= cost_difference:
                                                # Switch to gift card with sufficient funds
                                                payment_method_id = alt_method_id
                                                payment_method = alt_method
                                                # Add a note about the automatic switch
                                                if "payment_method_auto_switched" not in target_reservation:
                                                    target_reservation["payment_method_auto_switched"] = []
                                                # Get flight date for deterministic timestamp
                                                flight_date = target_reservation.get("flights", [{}])[0].get("date") if target_reservation.get("flights") else None
                                                target_reservation["payment_method_auto_switched"].append({
                                                    "original_method": original_payment_method_id,
                                                    "switched_to": alt_method_id,
                                                    "reason": "insufficient_funds",
                                                    "timestamp": generate_deterministic_timestamp(reservation_id, flight_date)
                                                })
                                                break
                                else:
                                    # No suitable alternative found, return error with suggestions
                                    return json.dumps({
                                        "status": "insufficient_funds",
                                        "message": f"The payment method '{payment_method_id}' has insufficient funds. Available: ${available_amount}, Required: ${cost_difference}. Alternative payment methods: {', '.join(alternative_methods)}",
                                        "payment_method_id": payment_method_id,
                                        "available_amount": available_amount,
                                        "required_amount": cost_difference,
                                        "alternative_payment_methods": alternative_methods
                                    })
                            else:
                                return json.dumps({
                                    "status": "insufficient_funds",
                                    "message": f"The payment method '{payment_method_id}' has insufficient funds. Available: ${available_amount}, Required: ${cost_difference}. No alternative payment methods with sufficient funds found.",
                                    "payment_method_id": payment_method_id,
                                    "available_amount": available_amount,
                                    "required_amount": cost_difference
                                })



                if cost_difference != 0 and payment_method_id is not None:
                    if "payment_history" not in target_reservation:
                        target_reservation["payment_history"] = []

                    target_reservation["payment_history"].append({
                        "payment_id": payment_method_id or "no_payment_method",
                        "amount": cost_difference
                    })

                    # Only process payment method adjustments if payment_method is defined and payment_method_id exists
                    if payment_method and payment_method_id and payment_method["source"] in ["gift_card", "certificate"]:
                        if cost_difference > 0:  # Additional charge
                            new_amount = payment_method["amount"] - cost_difference
                            data["users"][user_index]["payment_methods"][payment_method_id]["amount"] = new_amount
                        elif cost_difference < 0:  # Refund
                            new_amount = payment_method["amount"] + abs(cost_difference)
                            data["users"][user_index]["payment_methods"][payment_method_id]["amount"] = new_amount

                    payment_processed = True
                    updates_made.append("payment")

        target_reservation["total_cost"] = new_total_cost + cabin_upgrade_cost

        data["reservations"][reservation_index] = target_reservation

        flights = target_reservation.get("flights", [])
        passengers = target_reservation.get("passengers", [])
        trip_summary = {
            "total_flights": len(flights),
            "total_cost": new_total_cost + cabin_upgrade_cost,
            "departure_date": flights[0].get("date") if flights else None,
            "return_date": flights[-1].get("date") if len(flights) > 1 else None,
            "passenger_count": len(passengers)
        }

        response = {
            "success": True,
            "message": "Reservation updated successfully",
            "reservation_id": reservation_id,
            "updates_made": updates_made,
            "trip_summary": trip_summary,
            "updated_reservation": target_reservation
        }

        # Add information about automatic payment method selection if applicable
        if "payment_method_auto_selected" in target_reservation:
            latest_auto_selection = target_reservation["payment_method_auto_selected"][-1]
            response["payment_method_note"] = {
                "message": f"Payment method automatically selected: {latest_auto_selection['auto_selected']} (originally requested: {latest_auto_selection['original_requested']})",
                "auto_selected_method": latest_auto_selection['auto_selected'],
                "original_requested": latest_auto_selection['original_requested']
            }

        # Add information about automatic payment method switching if applicable
        if "payment_method_auto_switched" in target_reservation:
            latest_auto_switch = target_reservation["payment_method_auto_switched"][-1]
            response["payment_method_switch_note"] = {
                "message": f"Payment method automatically switched from {latest_auto_switch['original_method']} to {latest_auto_switch['switched_to']} due to insufficient funds",
                "original_method": latest_auto_switch['original_method'],
                "switched_to": latest_auto_switch['switched_to'],
                "reason": latest_auto_switch['reason']
            }

        if payment_processed:
            response["payment_adjustment"] = {
                "cost_difference": cost_difference,
                "new_total_cost": new_total_cost + cabin_upgrade_cost,
                "original_total_cost": original_total_cost,
                "cabin_upgrade_cost": cabin_upgrade_cost if cabin_upgrade_cost != 0 else None
            }

        # Add payment method information to response
        if payment_method_id is not None:
            response["payment_method_used"] = payment_method_id

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation",
                "description": "Modify existing flight reservations. Allows updating flights, passengers, cabin class, baggage, insurance, and payment methods. Automatically handles payment adjustments for cost changes. Supports cabin classes: basic_economy, economy, business, first. Payment methods include credit cards (Visa, Mastercard), gift cards, and certificates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Unique reservation identifier to update"
                        },
                        "flights": {
                            "type": "array",
                            "description": "Updated flight segments. Each flight must include origin, destination, flight_number, date (YYYY-MM-DD), and price. Flight numbers follow HAT### format",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "origin": {"type": "string", "description": "Origin airport IATA code"},
                                    "destination": {"type": "string", "description": "Destination airport IATA code"},
                                    "flight_number": {"type": "string", "description": "Flight number in HAT### format"},
                                    "date": {"type": "string", "description": "Flight date in YYYY-MM-DD format"},
                                    "price": {"type": "number", "description": "Flight price in USD"}
                                }
                            }
                        },
                        "passengers": {
                            "type": "array",
                            "description": "Updated passenger list. Each passenger must include first_name, last_name, and dob (YYYY-MM-DD)",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string", "description": "Passenger first name"},
                                    "last_name": {"type": "string", "description": "Passenger last name"},
                                    "dob": {"type": "string", "description": "Date of birth in YYYY-MM-DD format"}
                                }
                            }
                        },
                        "cabin": {
                            "type": "string",
                            "description": "Updated cabin class: 'basic_economy', 'economy', 'business', or 'first'. Available options based on aircraft configuration and route."
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Updated total number of baggage items. Includes both free and paid baggage allowances."
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Updated number of paid baggage items. Additional bags beyond free allowance incur charges."
                        },
                        "insurance": {
                            "type": "string",
                            "description": "Updated travel insurance option: 'yes' or 'no'. Covers trip cancellation, medical emergencies, and baggage loss."
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "Payment method ID for processing cost differences."
                        }
                    },
                    "required": ["reservation_id"]
                }
            }
        }
