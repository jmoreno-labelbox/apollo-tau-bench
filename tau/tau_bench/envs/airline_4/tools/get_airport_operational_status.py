from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetAirportOperationalStatus(Tool):
    """API tool for retrieving airport status and runway information along with operational details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        iata_code: str | None = None,
        airport_id: str | None = None,
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not iata_code and not airport_id:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either iata_code or airport_id must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Locate the airport
        airports = data.get("airports", [])
        target_airport = None

        for airport in airports:
            if (iata_code and airport.get("iata_code") == iata_code) or (
                airport_id and airport.get("airport_id") == airport_id
            ):
                target_airport = airport
                break

        if not target_airport:
            search_criteria = (
                {"iata_code": iata_code} if iata_code else {"airport_id": airport_id}
            )
            payload = {"error": "Airport not found", "search_criteria": search_criteria}
            out = json.dumps(
                payload)
            return out

        #Obtain information about the airport
        airport_info = {
            "airport_id": target_airport.get("airport_id"),
            "iata_code": target_airport.get("iata_code"),
            "icao_code": target_airport.get("icao_code"),
            "airport_name": target_airport.get("airport_name"),
            "location": target_airport.get("location", {}),
            "timezone": target_airport.get("timezone"),
            "operational_status": target_airport.get("operational_status"),
        }

        #Handle information regarding runways
        runways = target_airport.get("runways", [])
        runway_analysis = {
            "total_runways": len(runways),
            "runway_details": runways,
            "surface_types": {},
            "longest_runway": None,
            "shortest_runway": None,
        }

        #Examine the runways
        if runways:
            #Tally the types of surfaces
            for runway in runways:
                surface = runway.get("surface_type", "Unknown")
                runway_analysis["surface_types"][surface] = (
                    runway_analysis["surface_types"].get(surface, 0) + 1
                )

            #Identify the longest and shortest runways
            runway_lengths = [(r.get("length_meters", 0), r) for r in runways]
            runway_lengths.sort(key=lambda x: x[0])

            if runway_lengths:
                runway_analysis["shortest_runway"] = {
                    "designator": runway_lengths[0][1].get("designator"),
                    "length_meters": runway_lengths[0][0],
                    "surface_type": runway_lengths[0][1].get("surface_type"),
                }
                runway_analysis["longest_runway"] = {
                    "designator": runway_lengths[-1][1].get("designator"),
                    "length_meters": runway_lengths[-1][0],
                    "surface_type": runway_lengths[-1][1].get("surface_type"),
                }

        #Locate current flights at this airport
        flights = data.get("flights", [])
        current_flights = {"departures": [], "arrivals": []}

        for flight in flights:
            flight_origin = flight.get("origin")
            flight_dest = flight.get("destination")

            #Verify if this airport is associated with any flights
            if flight_origin == target_airport.get("iata_code"):
                #This represents a departure
                current_flights["departures"].append(
                    {
                        "flight_number": flight.get("flight_number"),
                        "destination": flight_dest,
                        "scheduled_departure_time_est": flight.get(
                            "scheduled_departure_time_est"
                        ),
                    }
                )
            elif flight_dest == target_airport.get("iata_code"):
                #This signifies an arrival
                current_flights["arrivals"].append(
                    {
                        "flight_number": flight.get("flight_number"),
                        "origin": flight_origin,
                        "scheduled_arrival_time_est": flight.get(
                            "scheduled_arrival_time_est"
                        ),
                    }
                )

        #Locate aircraft that are currently at this airport
        aircraft_data = data.get("aircraft", [])
        aircraft_at_airport = []

        for aircraft in aircraft_data:
            location = aircraft.get("location", {})
            if location.get("airport_id") == target_airport.get(
                "airport_id"
            ) or location.get("iata_code") == target_airport.get("iata_code"):
                aircraft_at_airport.append(
                    {
                        "aircraft_id": aircraft.get("aircraft_id"),
                        "tail_number": aircraft.get("tail_number"),
                        "model": aircraft.get("model", {}),
                        "status": aircraft.get("status"),
                    }
                )

        #Verify for operational events occurring at this airport
        operational_events = data.get("operational_events", [])
        airport_events = []

        for event in operational_events:
            event_airport = event.get("airport", {})
            if event_airport.get("airport_id") == target_airport.get(
                "airport_id"
            ) or event_airport.get("iata_code") == target_airport.get("iata_code"):
                airport_events.append(
                    {
                        "event_id": event.get("event_id"),
                        "event_type": event.get("event_type"),
                        "status": event.get("status"),
                        "event_timestamp_utc": event.get("event_timestamp_utc"),
                        "details": event.get("details"),
                    }
                )

        #Organize events by timestamp (latest first)
        airport_events.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Compute statistics related to operations
        operational_stats = {
            "total_departures": len(current_flights["departures"]),
            "total_arrivals": len(current_flights["arrivals"]),
            "aircraft_on_ground": len(aircraft_at_airport),
            "active_events": len(
                [e for e in airport_events if e.get("status") == "Active"]
            ),
            "recent_events": len(airport_events),
        }

        #Assess the overall health of operations
        operational_health = "Normal"
        health_factors = []

        if target_airport.get("operational_status") != "Operational":
            operational_health = "Limited"
            health_factors.append(
                f"Airport status: {target_airport.get('operational_status')}"
            )

        active_events = [e for e in airport_events if e.get("status") == "Active"]
        if active_events:
            operational_health = "Impacted"
            health_factors.append(f"{len(active_events)} active operational events")

        if not health_factors:
            health_factors.append("No operational issues detected")

        #Formulate response
        response = {
            "airport": airport_info,
            "runway_information": runway_analysis,
            "current_operations": {
                "flights": current_flights,
                "aircraft_on_ground": aircraft_at_airport,
                "statistics": operational_stats,
            },
            "operational_events": {
                "recent_events": airport_events[:10],  #Latest 10 events
                "total_events": len(airport_events),
            },
            "operational_health": {
                "status": operational_health,
                "factors": health_factors,
            },
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAirportOperationalStatus",
                "description": "Get comprehensive airport status and runway information with operational details including current flights, aircraft, and events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "Airport IATA code (e.g., 'ATL', 'DFW'). Either this or airport_id must be provided.",
                        },
                        "airport_id": {
                            "type": "string",
                            "description": "Airport ID (e.g., 'ARP_ATL'). Either this or iata_code must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }
