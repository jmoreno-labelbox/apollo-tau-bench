from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateShippingCost(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        destination_country: str,
        total_items: int,
        order_value: float,
        location: dict[str, str] = None,
        courier_id: str = None
,
    address: Any = None,
    ) -> str:
        """
        Calculate shipping cost based on destination, weight, order value, optional detailed location, and specific courier selection

        Data Sources: couriers.json (courier_id, name, coverage_area, contact_info, base_cost, rating, service_types)
        """
        pass
        #Rule: Assign couriers only if destination country matches their coverage areas
        couriers = data.get("couriers", {}).values()
        eligible_couriers = []

        for courier in couriers.values()):
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_data["couriers"][courier_id] = courier

        if not eligible_couriers:
            payload = {
                    "error": f"No shipping service available to {destination_country}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Select courier based on courier_id parameter or use automatic selection
        selected_courier = None
        courier_selection_method = "automatic"

        if courier_id:
            #Find the specific courier if provided
            selected_courier = next(
                (c for c in eligible_couriers if c.get("courier_id") == courier_id),
                None,
            )

            if not selected_courier:
                payload = {
                        "error": f"Courier {courier_id} not available for destination {destination_country} or does not exist",
                        "status": "failed",
                        "available_couriers": [
                            {"courier_id": c.get("courier_id"), "name": c.get("name")}
                            for c in eligible_couriers
                        ],
                    }
                out = json.dumps(
                    payload)
                return out
            courier_selection_method = "specific"
        else:
            #Use automatic selection logic (first available courier)
            selected_courier = eligible_couriers[0]

        #Process location information if provided
        delivery_location = None
        location_surcharge = 0.0

        if location:
            #Validate location has required fields
            required_location_fields = ["city", "country"]
            missing_fields = [
                field for field in required_location_fields if not location.get(field)
            ]

            if missing_fields:
                payload = {
                        "error": f"Location missing required fields: {', '.join(missing_fields)}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            delivery_location = {
                "address1": location.get("address1", ""),
                "address2": location.get("address2", ""),
                "city": location.get("city"),
                "state": location.get("state", ""),
                "zip": location.get("zip", ""),
                "country": location.get("country"),
            }

            #Verify location country matches destination_country parameter
            if delivery_location["country"] != destination_country:
                payload = {
                        "error": f"Location country '{delivery_location['country']}' does not match destination_country '{destination_country}'",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #Apply location-based surcharges (simplified logic)
            city = delivery_location["city"].lower()
            delivery_location.get("state", "").lower()

            #Remote area surcharge for certain locations
            remote_cities = ["anchorage", "honolulu", "fairbanks", "juneau"]
            if city in remote_cities:
                location_surcharge += 25.0

            #Rural area surcharge based on ZIP code patterns (simplified)
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Example: certain ZIP code ranges might be considered rural
                if zip_code.startswith(("9999", "0000")):  #Placeholder logic
                    location_surcharge += 10.0

        #Get courier-specific pricing information
        courier_base_cost = selected_courier.get("base_cost", 9.99)
        courier_rating = selected_courier.get("rating", 0)
        courier_service_types = selected_courier.get("service_types", ["standard"])
        courier_specialties = selected_courier.get("specialties", [])

        #Calculate courier-specific adjustments
        courier_adjustment = 0.0
        service_quality_bonus = 0.0

        #Premium pricing for high-rated couriers
        if courier_rating >= 4.5:
            service_quality_bonus = 2.00  #Premium service surcharge
        elif courier_rating >= 4.0:
            service_quality_bonus = 1.00  #Good service slight surcharge
        elif courier_rating < 3.0:
            courier_adjustment = -1.00  #Discount for lower-rated couriers

        #Service type adjustments
        service_type_surcharge = 0.0
        courier_service_types[0] if courier_service_types else "standard"

        if "express" in courier_service_types:
            service_type_surcharge = 5.00
        elif "overnight" in courier_service_types:
            service_type_surcharge = 15.00
        elif "same-day" in courier_service_types:
            service_type_surcharge = 25.00

        #Specialty service adjustments
        specialty_adjustment = 0.0
        if "urban" in courier_specialties and location:
            city = delivery_location["city"].lower()
            major_cities = ["new york", "los angeles", "chicago", "houston", "phoenix"]
            if city in major_cities:
                specialty_adjustment = (
                    -2.00
                )  #Discount for urban specialists in major cities

        if "rural" in courier_specialties and location:
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Rural areas benefit from rural specialists
                if not zip_code.startswith(
                    ("100", "200", "300", "400", "500")
                ):  #Non-major metro areas
                    specialty_adjustment = -3.00

        #Basic shipping cost calculation with courier-specific base cost
        base_cost = courier_base_cost
        weight_cost = total_items * 2.50  #$2.50 per unit weight

        #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        insurance_required = order_value > 1000.0
        insurance_cost = (
            (order_value * 0.015) if insurance_required else 0
        )  #1.5% of order value

        #International shipping surcharge
        international_surcharge = 15.00 if destination_country != "USA" else 0

        #Calculate total shipping cost with all adjustments
        total_shipping_cost = (
            base_cost
            + weight_cost
            + insurance_cost
            + international_surcharge
            + location_surcharge
            + courier_adjustment
            + service_quality_bonus
            + service_type_surcharge
            + specialty_adjustment
        )

        #Ensure minimum shipping cost
        total_shipping_cost = max(total_shipping_cost, 5.00)  #Minimum $5.00 shipping

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
                    "contact_info": selected_courier.get("contact_info"),
                },
                "selection_method": courier_selection_method,
                "courier_requested": courier_id is not None,
                "alternative_couriers_available": len(eligible_couriers) - 1,
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
                    "specialty_adjustment": round(specialty_adjustment, 2),
                },
                "total_cost": round(total_shipping_cost, 2),
            },
            "order_details": {
                "item_total": total_items,
                "value": order_value,
                "requires_insurance": insurance_required,
            },
            "courier_comparison": {
                "selected_courier_cost": round(total_shipping_cost, 2),
                "available_alternatives": len(eligible_couriers) - 1,
                "cost_factors": {
                    "courier_rating_impact": (
                        f"+${service_quality_bonus:.2f}"
                        if service_quality_bonus > 0
                        else f"${courier_adjustment:.2f}"
                    )
                }
            }
        }
        
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        eligible_couriers = []

        for courier in couriers.values():
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_data["couriers"][courier_id] = courier

        if not eligible_couriers:
            payload = {
                    "error": f"No shipping service available to {destination_country}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Select courier based on courier_id parameter or use automatic selection
        selected_courier = None
        courier_selection_method = "automatic"

        if courier_id:
            #Find the specific courier if provided
            selected_courier = next(
                (c for c in eligible_couriers if c.get("courier_id") == courier_id),
                None,
            )

            if not selected_courier:
                payload = {
                        "error": f"Courier {courier_id} not available for destination {destination_country} or does not exist",
                        "status": "failed",
                        "available_couriers": [
                            {"courier_id": c.get("courier_id"), "name": c.get("name")}
                            for c in eligible_couriers
                        ],
                    }
                out = json.dumps(
                    payload)
                return out
            courier_selection_method = "specific"
        else:
            #Use automatic selection logic (first available courier)
            selected_courier = eligible_couriers[0]

        #Process location information if provided
        delivery_location = None
        location_surcharge = 0.0

        if location:
            #Validate location has required fields
            required_location_fields = ["city", "country"]
            missing_fields = [
                field for field in required_location_fields if not location.get(field)
            ]

            if missing_fields:
                payload = {
                        "error": f"Location missing required fields: {', '.join(missing_fields)}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            delivery_location = {
                "address1": location.get("address1", ""),
                "address2": location.get("address2", ""),
                "city": location.get("city"),
                "state": location.get("state", ""),
                "zip": location.get("zip", ""),
                "country": location.get("country"),
            }

            #Verify location country matches destination_country parameter
            if delivery_location["country"] != destination_country:
                payload = {
                        "error": f"Location country '{delivery_location['country']}' does not match destination_country '{destination_country}'",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #Apply location-based surcharges (simplified logic)
            city = delivery_location["city"].lower()
            delivery_location.get("state", "").lower()

            #Remote area surcharge for certain locations
            remote_cities = ["anchorage", "honolulu", "fairbanks", "juneau"]
            if city in remote_cities:
                location_surcharge += 25.0

            #Rural area surcharge based on ZIP code patterns (simplified)
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Example: certain ZIP code ranges might be considered rural
                if zip_code.startswith(("9999", "0000")):  #Placeholder logic
                    location_surcharge += 10.0

        #Get courier-specific pricing information
        courier_base_cost = selected_courier.get("base_cost", 9.99)
        courier_rating = selected_courier.get("rating", 0)
        courier_service_types = selected_courier.get("service_types", ["standard"])
        courier_specialties = selected_courier.get("specialties", [])

        #Calculate courier-specific adjustments
        courier_adjustment = 0.0
        service_quality_bonus = 0.0

        #Premium pricing for high-rated couriers
        if courier_rating >= 4.5:
            service_quality_bonus = 2.00  #Premium service surcharge
        elif courier_rating >= 4.0:
            service_quality_bonus = 1.00  #Good service slight surcharge
        elif courier_rating < 3.0:
            courier_adjustment = -1.00  #Discount for lower-rated couriers

        #Service type adjustments
        service_type_surcharge = 0.0
        courier_service_types[0] if courier_service_types else "standard"

        if "express" in courier_service_types:
            service_type_surcharge = 5.00
        elif "overnight" in courier_service_types:
            service_type_surcharge = 15.00
        elif "same-day" in courier_service_types:
            service_type_surcharge = 25.00

        #Specialty service adjustments
        specialty_adjustment = 0.0
        if "urban" in courier_specialties and location:
            city = delivery_location["city"].lower()
            major_cities = ["new york", "los angeles", "chicago", "houston", "phoenix"]
            if city in major_cities:
                specialty_adjustment = (
                    -2.00
                )  #Discount for urban specialists in major cities

        if "rural" in courier_specialties and location:
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Rural areas benefit from rural specialists
                if not zip_code.startswith(
                    ("100", "200", "300", "400", "500")
                ):  #Non-major metro areas
                    specialty_adjustment = -3.00

        #Basic shipping cost calculation with courier-specific base cost
        base_cost = courier_base_cost
        weight_cost = total_items * 2.50  #$2.50 per unit weight

        #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        insurance_required = order_value > 1000.0
        insurance_cost = (
            (order_value * 0.015) if insurance_required else 0
        )  #1.5% of order value

        #International shipping surcharge
        international_surcharge = 15.00 if destination_country != "USA" else 0

        #Calculate total shipping cost with all adjustments
        total_shipping_cost = (
            base_cost
            + weight_cost
            + insurance_cost
            + international_surcharge
            + location_surcharge
            + courier_adjustment
            + service_quality_bonus
            + service_type_surcharge
            + specialty_adjustment
        )

        #Ensure minimum shipping cost
        total_shipping_cost = max(total_shipping_cost, 5.00)  #Minimum $5.00 shipping

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
                    "contact_info": selected_courier.get("contact_info"),
                },
                "selection_method": courier_selection_method,
                "courier_requested": courier_id is not None,
                "alternative_couriers_available": len(eligible_couriers) - 1,
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
                    "specialty_adjustment": round(specialty_adjustment, 2),
                },
                "total_cost": round(total_shipping_cost, 2),
            },
            "order_details": {
                "item_total": total_items,
                "value": order_value,
                "requires_insurance": insurance_required,
            },
            "courier_comparison": {
                "selected_courier_cost": round(total_shipping_cost, 2),
                "available_alternatives": len(eligible_couriers) - 1,
                "cost_factors": {
                    "courier_rating_impact": (
                        f"+${service_quality_bonus:.2f}"
                        if service_quality_bonus > 0
                        else f"${courier_adjustment:.2f}"
                    ),
                    "service_type_impact": (
                        f"+${service_type_surcharge:.2f}"
                        if service_type_surcharge > 0
                        else "$0.00"
                    ),
                    "specialty_discount": (
                        f"${specialty_adjustment:.2f}"
                        if specialty_adjustment != 0
                        else "$0.00"
                    ),
                },
            },
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateShippingCost",
                "description": "Calculate shipping cost based on destination, order characteristics, optional detailed location, and optional specific courier selection with courier-specific pricing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {
                            "type": "string",
                            "description": "Destination country for shipping",
                        },
                        "total_items": {
                            "type": "number",
                            "description": "Total number of items",
                        },
                        "order_value": {
                            "type": "number",
                            "description": "Order value in dollars",
                        },
                        "location": {
                            "type": "object",
                            "properties": {
                                "address1": {
                                    "type": "string",
                                    "description": "Primary street address",
                                },
                                "address2": {
                                    "type": "string",
                                    "description": "Secondary address line (apartment, suite, etc.)",
                                },
                                "city": {"type": "string", "description": "City name"},
                                "state": {
                                    "type": "string",
                                    "description": "State or province",
                                },
                                "zip": {
                                    "type": "string",
                                    "description": "ZIP or postal code",
                                },
                                "country": {
                                    "type": "string",
                                    "description": "Country name",
                                },
                            },
                            "required": ["city", "country"],
                            "description": "Optional detailed delivery address for location-based pricing",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional specific courier ID to use for shipping calculation. If provided, calculates cost using that courier's specific pricing, ratings, and service capabilities.",
                        },
                    },
                    "required": ["destination_country", "total_items", "order_value"],
                },
            },
        }

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateShippingCost",
                "description": "Calculate shipping cost based on destination, order characteristics, optional detailed location, and optional specific courier selection with courier-specific pricing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {
                            "type": "string",
                            "description": "Destination country for shipping",
                        },
                        "total_items": {
                            "type": "number",
                            "description": "Total number of items",
                        },
                        "order_value": {
                            "type": "number",
                            "description": "Order value in dollars",
                        },
                        "location": {
                            "type": "object",
                            "properties": {
                                "address1": {
                                    "type": "string",
                                    "description": "Primary street address",
                                },
                                "address2": {
                                    "type": "string",
                                    "description": "Secondary address line (apartment, suite, etc.)",
                                },
                                "city": {"type": "string", "description": "City name"},
                                "state": {
                                    "type": "string",
                                    "description": "State or province",
                                },
                                "zip": {
                                    "type": "string",
                                    "description": "ZIP or postal code",
                                },
                                "country": {
                                    "type": "string",
                                    "description": "Country name",
                                },
                            },
                            "required": ["city", "country"],
                            "description": "Optional detailed delivery address for location-based pricing",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional specific courier ID to use for shipping calculation. If provided, calculates cost using that courier's specific pricing, ratings, and service capabilities.",
                        },
                    },
                    "required": ["destination_country", "total_items", "order_value"],
                },
            },
        }
