# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateShippingCost(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], destination_country: str, total_items: int, order_value: float, location: Dict[str, str] = None, courier_id: str = None, **kwargs) -> str:
        """
        Calculate shipping cost based on destination, weight, order value, optional detailed location, and specific courier selection

        Data Sources: couriers.json (courier_id, name, coverage_area, contact_info, base_cost, rating, service_types)
        """
        # Condition: Assign couriers solely when the destination country is within their service regions.
        couriers = data.get("couriers", [])
        eligible_couriers = []

        for courier in couriers:
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_couriers.append(courier)

        if not eligible_couriers:
            return json.dumps({
                "error": f"No shipping service available to {destination_country}",
                "status": "failed"
            })

        # Choose the courier using the courier_id parameter or opt for automatic selection.
        selected_courier = None
        courier_selection_method = "automatic"

        if courier_id:
            # Identify the designated courier if available.
            selected_courier = next((c for c in eligible_couriers if c.get("courier_id") == courier_id), None)

            if not selected_courier:
                return json.dumps({
                    "error": f"Courier {courier_id} not available for destination {destination_country} or does not exist",
                    "status": "failed",
                    "available_couriers": [{"courier_id": c.get("courier_id"), "name": c.get("name")} for c in eligible_couriers]
                })
            courier_selection_method = "specific"
        else:
            # Implement automatic courier selection (first available option).
            selected_courier = eligible_couriers[0]

        # Handle location data if available.
        delivery_location = None
        location_surcharge = 0.0

        if location:
            # Check that the location contains all necessary fields.
            required_location_fields = ["city", "country"]
            missing_fields = [field for field in required_location_fields if not location.get(field)]

            if missing_fields:
                return json.dumps({
                    "error": f"Location missing required fields: {', '.join(missing_fields)}",
                    "status": "failed"
                })

            delivery_location = {
                "address1": location.get("address1", ""),
                "address2": location.get("address2", ""),
                "city": location.get("city"),
                "state": location.get("state", ""),
                "zip": location.get("zip", ""),
                "country": location.get("country")
            }

            # Check if the location's country corresponds to the destination_country parameter.
            if delivery_location["country"] != destination_country:
                return json.dumps({
                    "error": f"Location country '{delivery_location['country']}' does not match destination_country '{destination_country}'",
                    "status": "failed"
                })

            # Implement location-dependent fees (streamlined approach)
            city = delivery_location["city"].lower()
            state = delivery_location.get("state", "").lower()

            # Additional fee for specific remote locations.
            remote_cities = ["anchorage", "honolulu", "fairbanks", "juneau"]
            if city in remote_cities:
                location_surcharge += 25.0

            # Surcharge for rural areas determined by ZIP code trends (simplified)
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                # Specific ZIP code ranges may be classified as rural.
                if zip_code.startswith(("9999", "0000")):  # Stub functionality
                    location_surcharge += 10.0

        # Retrieve pricing details specific to the courier.
        courier_base_cost = selected_courier.get("base_cost", 9.99)
        courier_rating = selected_courier.get("rating", 0)
        courier_service_types = selected_courier.get("service_types", ["standard"])
        courier_specialties = selected_courier.get("specialties", [])

        # Compute adjustments specific to the courier.
        courier_adjustment = 0.0
        service_quality_bonus = 0.0

        # Elevated pricing for top-rated delivery personnel.
        if courier_rating >= 4.5:
            service_quality_bonus = 2.00  # Additional fee for premium service
        elif courier_rating >= 4.0:
            service_quality_bonus = 1.00  # Quality service with a minor additional fee.
        elif courier_rating < 3.0:
            courier_adjustment = -1.00  # Reduced fees for couriers with lower ratings

        # Modifications to service type
        service_type_surcharge = 0.0
        primary_service_type = courier_service_types[0] if courier_service_types else "standard"

        if "express" in courier_service_types:
            service_type_surcharge = 5.00
        elif "overnight" in courier_service_types:
            service_type_surcharge = 15.00
        elif "same-day" in courier_service_types:
            service_type_surcharge = 25.00

        # Modifications to specialized services
        specialty_adjustment = 0.0
        if "urban" in courier_specialties and location:
            city = delivery_location["city"].lower()
            major_cities = ["new york", "los angeles", "chicago", "houston", "phoenix"]
            if city in major_cities:
                specialty_adjustment = -2.00  # Reduction for urban experts in key metropolitan areas.

        if "rural" in courier_specialties and location:
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                # Rural regions gain advantages from specialists in rural fields.
                if not zip_code.startswith(("100", "200", "300", "400", "500")):  # Minor metropolitan regions
                    specialty_adjustment = -3.00

        # Fundamental shipping fee computation using base rates specific to the courier.
        base_cost = courier_base_cost
        weight_cost = total_items * 2.50  # $2.50 for each unit of weight

        # Policy: Orders exceeding $1000 must undergo payment verification prior to processing.
        insurance_required = order_value > 1000.0
        insurance_cost = (order_value * 0.015) if insurance_required else 0  # 1.5% of the total order amount

        # Additional fee for international shipping
        international_surcharge = 15.00 if destination_country != "USA" else 0

        # Compute the overall shipping expenses including all modifications.
        total_shipping_cost = (
            base_cost +
            weight_cost +
            insurance_cost +
            international_surcharge +
            location_surcharge +
            courier_adjustment +
            service_quality_bonus +
            service_type_surcharge +
            specialty_adjustment
        )

        # Optimize for lowest shipping expense.
        total_shipping_cost = max(total_shipping_cost, 5.00)  # Shipping starts at $5.00.

        result = {
            "status": "success",
            "destination_country": destination_country,
            "delivery_location": delivery_location,
            "courier_selection": {
                "selected_courier": {
                    "courier_id": selected_courier.get("courier_id"),
                    "name": selected_courier.get("name"),
                    "rating": courier_rating,
                    "service_types": courier_service_types,
                    "specialties": courier_specialties,
                    "contact_info": selected_courier.get("contact_info")
                },
                "selection_method": courier_selection_method,
                "courier_requested": courier_id is not None,
                "alternative_couriers_available": len(eligible_couriers) - 1
            },
            "shipping_breakdown": {
                "base_cost": courier_base_cost,
                "weight_cost": round(weight_cost, 2),
                "insurance_cost": round(insurance_cost, 2),
                "international_surcharge": international_surcharge,
                "location_surcharge": round(location_surcharge, 2),
                "courier_adjustments": {
                    "courier_base_adjustment": round(courier_adjustment, 2),
                    "service_quality_bonus": round(service_quality_bonus, 2),
                    "service_type_surcharge": round(service_type_surcharge, 2),
                    "specialty_adjustment": round(specialty_adjustment, 2)
                },
                "total_cost": round(total_shipping_cost, 2)
            },
            "order_details": {
                "item_total": total_items,
                "value": order_value,
                "requires_insurance": insurance_required
            },
            "courier_comparison": {
                "selected_courier_cost": round(total_shipping_cost, 2),
                "available_alternatives": len(eligible_couriers) - 1,
                "cost_factors": {
                    "courier_rating_impact": f"+${service_quality_bonus:.2f}" if service_quality_bonus > 0 else f"${courier_adjustment:.2f}",
                    "service_type_impact": f"+${service_type_surcharge:.2f}" if service_type_surcharge > 0 else "$0.00",
                    "specialty_discount": f"${specialty_adjustment:.2f}" if specialty_adjustment != 0 else "$0.00"
                }
            }
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_shipping_cost",
                "description": "Calculate shipping cost based on destination, order characteristics, optional detailed location, and optional specific courier selection with courier-specific pricing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {"type": "string", "description": "Destination country for shipping"},
                        "total_items": {"type": "number", "description": "Total number of items"},
                        "order_value": {"type": "number", "description": "Order value in dollars"},
                        "location": {
                            "type": "object",
                            "properties": {
                                "address1": {"type": "string", "description": "Primary street address"},
                                "address2": {"type": "string", "description": "Secondary address line (apartment, suite, etc.)"},
                                "city": {"type": "string", "description": "City name"},
                                "state": {"type": "string", "description": "State or province"},
                                "zip": {"type": "string", "description": "ZIP or postal code"},
                                "country": {"type": "string", "description": "Country name"}
                            },
                            "required": ["city", "country"],
                            "description": "Optional detailed delivery address for location-based pricing"
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional specific courier ID to use for shipping calculation. If provided, calculates cost using that courier's specific pricing, ratings, and service capabilities."
                        }
                    },
                    "required": ["destination_country", "total_items", "order_value"]
                }
            }
        }
