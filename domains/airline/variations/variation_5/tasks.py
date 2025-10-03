from domains.dto import Action, Task


TASKS = [
    Task(
        annotator="0",
        user_id="USER_001",
        instruction=(
            "Execute HQ Ops+Pricing analysis duties. You want flight HAT001 to be available on 2024-05-03, and—on "
            "2024-05-17—you want it available with available_seats={'basic_economy':16,'economy':13,'business':9} "
            "and prices={'basic_economy':76,'economy':189,'business':498}. You want confirmation of the "
            "flight_status for 2024-05-03 and—for 2024-05-17—the available_seats and prices above."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-03"],
                "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-17"],
                "status": "available"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-17",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-03"
            }),
            Action(name="GetAvailableSeat", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-17",
                "cabin": "basic_economy"
            }),
        ],
        outputs=[
            '"operating_date": "2024-05-03"',
            '"flight_status": "available"',
            '"available_seats": {"basic_economy": 16, "economy": 13, "business": 9}',
            '"prices": {"basic_economy": 76, "economy": 189, "business": 498}'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_002",
        instruction=(
            "Execute HQ Pricing analysis duties. You want an audit snapshot for flight HAT197 on 2024-05-17. You need the flight to be operating (status ‘available’) with base fares on that date exactly: Basic Economy = 76, Economy = 189, Business = 498. You also need the Economy average price for 2024-05-16..2024-05-18 (min_samples = 1). Return only a concise verification summary with: operating_date, flight_status, the prices for 2024-05-17, and the computed average_price. Limit scope strictly to HAT197 and those dates."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT197",
                "dates": ["2024-05-17"],
                "status": "available"
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT197", "date": "2024-05-17"
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT197", "date": "2024-05-17",
                "fare_class": "basic_economy", "price": 76
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT197", "date": "2024-05-17",
                "fare_class": "economy", "price": 189
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT197", "date": "2024-05-17",
                "fare_class": "business", "price": 498
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT197",
                "fare_class": "economy",
                "start_date": "2024-05-16",
                "end_date": "2024-05-18",
                "min_samples": 1
            }),
        ],
        outputs=[
            '"operating_date": "2024-05-17"',
            '"flight_status": "available"',
            '"prices": {"basic_economy": 76.0, "economy": 189.0, "business": 498.0}',
            '"average_price": 149.33',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_003",
        instruction=(
            "Execute HQ Pricing analysis duties. You want HAT090 and HAT223 seasonally neutral on base_fare "
            "for 2024-05-24 through 2024-05-26 (multiplier 1.00); where not neutral, you need them normalized "
            "idempotently to neutrality. After this you want a cheapest-leg audit for reservation 'PGAGLM' using the "
            "reservation’s cabin, constrained to operating legs only (status 'available' with seats>0) and "
            "without deriving from flight buckets when leg prices already exist (fallback_to_flights=false). "
            "Return only: reservation_id, cabin, and a single cheapest_leg with flight_number, date (ISO), price, "
            "and price_source. Scope is strictly those flights/dates and the given reservation."
        ),
        actions=[
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT090",
                "start_date": "2024-05-24",
                "end_date":   "2024-05-26",
                "multiplier": 1.00
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT223",
                "start_date": "2024-05-24",
                "end_date": "2024-05-26",
                "multiplier": 1.00
            }),
            Action(name="GetCheapestFlightFromReservation", kwargs={
                "reservation_id": "PGAGLM",
                "require_available": True,
                "fallback_to_flights": False
            }),
        ],
        outputs=[
            '"reservation_id": "PGAGLM"',
            '"cabin": "business"',
            '"cheapest_leg": {"flight_number": "HAT090", "date": "2024-05-24", "price": 559.0, "price_source": "reservation"}',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_004",
        instruction=(
            "Execute Pricing analysis duties at HQ. You want flight HAT010 to be scheduled as available on 2024-05-16 with "
            "aircraft A320, treating schedule updates as additive and idempotent (no removals; no crew changes). You want "
            "confirmation of the current base fares on 2024-05-16 for Basic Economy, Economy, and Business. Return only the "
            "date and the base fares for those cabins. Limit scope strictly to HAT010 and this date."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT010",
                "dates": ["2024-05-16"],
                "status": "available",
                "aircraft": "A320"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT010",
                "date": "2024-05-16",
                "fare_class": "basic_economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT010",
                "date": "2024-05-16",
                "fare_class": "economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT010",
                "date": "2024-05-16",
                "fare_class": "business"
            }),
        ],
        outputs=[
            '"date": "2024-05-16"',
            '"basic_economy_price": 50',
            '"economy_price": 150',
            '"business_price": 449',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction=(
            "Lead HQ pricing operations. You want an ATL→JFK corridor snapshot for 2024-05-23 through 2024-05-30 "
            "that shows the authoritative cheapest-by-date for Basic Economy on base_fare, restricted to operating "
            "options (status 'available' with seats >0) and applying policy tie-breakers including lexicographic flight number. "
            "For HAT233, you need its schedule normalized so that it is 'cancelled' on 2024-05-17 and 2024-05-19, "
            "with explicit readbacks of the status for those two dates. Scope is limited strictly to the ATL→JFK corridor "
            "and HAT233; return only the minimal verification fields."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT233",
                "dates": ["2024-05-17", "2024-05-19"],
                "status": "cancelled"
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT233",
                "date": "2024-05-17"
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT233",
                "date": "2024-05-19"
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "ATL",
                "destination": "JFK",
                "fare_class": "basic_economy",
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number",
                "start_date": "2024-05-23",
                "end_date": "2024-05-30"
            }),
        ],
        outputs=[
            '"route": {"origin": "ATL", "destination": "JFK"}',
            '"cheapest_by_date": [',
            '"flight_number": "HAT233"',
            '"date": "2024-05-17"',
            '"flight_status": "cancelled"',
            '"date": "2024-05-19"',
            '"flight_status": "cancelled"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_006",
        instruction=(
            "Execute Pricing analysis duties at HQ. Deliver an audit where HAT002 is normalized from 2024-05-23 through 2024-05-29 (inclusive): "
            "the flight is sellable (status='available') and seasonally neutral (multiplier 1.00, base_fare only; taxes/fees unchanged) across that window. "
            "Include a Business-cabin fare history read for internal audit. Choose and order compliant tool usage at your discretion, ensure idempotency, "
            "and limit scope strictly to HAT002 and the stated dates."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-23",
                "end_date": "2024-05-29",
                "status": "available"
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-23",
                "end_date": "2024-05-29",
                "multiplier": 1.00
            }),
            Action(name="GetHistoricalTicketPrices", kwargs={
                "flight_number": "HAT002",
                "fare_class": "business"
            }),
        ],
        outputs=[
            '"flight_number": "HAT002"',
            '"fare_class": "business"',
            '"history": "read"',
            '"start_date": "2024-05-23"',
            '"end_date": "2024-05-29"',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_007",
    instruction=(
        "Execute HQ Pricing analysis duties. You want a one-day upgrade and repricing audit for HAT090 and reservation PGAGLM on 2024-05-24. "
        "Outcomes (idempotent and limited strictly to these entities and date): "
        "(a) HAT090 is sellable that day (schedule status 'available'); "
        "(b) Business mirrors Economy at no charge for that date (base_fare only; taxes/fees unchanged); "
        "(c) the reservation is reconciled using the reservation’s own cabin mapping with strategy token 'match_bucket', "
        "considering only sellable inventory (require_available = true) and allowing fallback to published flight pricing when "
        "a leg lacks a bucket rate (fallback_to_flights = true), with cabins_source = 'reservation'; "
        "(d) each leg includes a price_source; and "
        "(e) an audit note records a no-charge upgrade for the HAT090 segment on 2024-05-24 with reason 'free upgrade alignment'. "
        "Return only success = true."
    ),
    actions=[
        Action(name="UpdateFlightSchedule", kwargs={
            "flight_number": "HAT090",
            "dates": ["2024-05-24"],
            "status": "available"
        }),
        Action(name="BulkUpgradeTicketPrices", kwargs={
            "flight_number": "HAT090",
            "start_date": "2024-05-24",
            "end_date":   "2024-05-24",
            "from_cabin": "economy",
            "to_cabin":   "business"
        }),
        Action(name="RepriceReservation", kwargs={
            "reservation_id": "PGAGLM",
            "strategy": "match_bucket",
            "require_available": True,
            "cabins_source": "reservation",
            "fallback_to_flights": True
        }),
        Action(name="LogUpgradeNoCharge", kwargs={
            "reservation_id": "PGAGLM",
            "flight_number": "HAT090",
            "date": "2024-05-24",
            "from_cabin": "economy",
            "to_cabin": "business",
            "reason": "free upgrade alignment"
        }),
    ],
    outputs=[
        '"success": True',
    ],
),
    Task(
        annotator="0",
        user_id="USER_008",
        instruction=(
            "Execute Pricing analysis duties at HQ. Establish seasonal neutrality for HAT001 over 2024-05-20, 2024-05-21, and 2024-05-22 with multiplier 1.00 "
            "(no net change). Then, for cabin 'basic_economy' over the same window, report base_fare statistics using an IQR outlier policy (method='iqr', k=1.5) "
            "with min_samples=3; if the minimum is not met, expand the window by 2 days once (max_expansions=1). Include median and sample count. "
            "Select and order compliant tool usage under policy and idempotency, and return only the computed average_price, median_price, and sample_size."
        ),
        actions=[
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-20",
                "end_date": "2024-05-22",
                "multiplier": 1.00
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT001",
                "fare_class": "basic_economy",
                "start_date": "2024-05-20",
                "end_date": "2024-05-22",
                "price_component": "base_fare",
                "outlier_policy": {"method": "iqr", "k": 1.5},
                "min_samples": 3,
                "fallback": {"expand_window_days": 2, "max_expansions": 1},
                "include": {"median": True, "count": True}
            }),
        ],
        outputs=[
            '"average_price":  71.0',
            '"median_price": 70.0',
            '"sample_size": 3'
        ]
    ),
    # Hard version
    Task(
        annotator="0",
        user_id="USER_009",
        instruction=(
            "Lead fleet operations. You want storage and ferry handling for AC008 (ATR72-600) verified end-to-end, and then a "
            "clean price publication for HAT021 on 2024-05-23 without altering seat counts.\n\n"
            "Required end-state:\n"
            "(a) AC008 remains status 'stored' with reason 'remain parked';\n"
            "(b) AC008 location is LAS (confirmed via aircraft profile);\n"
            "(c) a LAS presence check filtered by model_id 'ATR72-600' lists AC008;\n"
            "(d) AC008 is assigned to operate HAT021 on 2024-05-23 (assignment must not modify stored status);\n"
            "(e) HAT021 on 2024-05-23 is 'available' and published prices (base_fare only) are exactly: "
            "basic_economy=76.00, economy=189.00, business=498.00 with seats unchanged;\n"
            "(f) the relocation to LAS is recorded with reason exactly 'short-term storage rotation'.\n\n"
            "Operate strictly on AC008 and HAT021 for that date. Use per-cabin atomic price writes; do not write seats. "
            "Return only minimal verification."
        ),
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC008", "status": "stored", "reason": "remain parked"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC008", "to_iata": "LAS", "reason": "short-term storage rotation"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC008"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "LAS", "model_id": "ATR72-600"}),

            # publish flight, then per-cabin price writes (no seats!)
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT021", "dates": ["2024-05-23"], "status": "available"
            }),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT021", "date": "2024-05-23", "new_aircraft_id": "AC008"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT021", "date": "2024-05-23",
                "prices": {"basic_economy": 76.00}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT021", "date": "2024-05-23",
                "prices": {"economy": 189.00}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT021", "date": "2024-05-23",
                "prices": {"business": 498.00}
            }),
        ],
        outputs=[
            '"aircraft_id":"AC008"', '"status":"stored"', '"reason":"remain parked"',
            '"iata_code":"LAS"', '"model_id":"ATR72-600"',
            '"flight_number":"HAT021"', '"date":"2024-05-23"', '"status":"available"',
            '"fare_class":"basic_economy"', '"price":76.0',
            '"fare_class":"economy"', '"price":189.0',
            '"fare_class":"business"', '"price":498.0'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_010",
        instruction=(
            "Execute Pricing analysis duties at HQ. You want a PHL→LGA corridor snapshot for May 2024 and to confirm operating eligibility on 2024-05-23. "
            "You need to verify: (a) HAT096 and HAT296 are sellable (status='available') on 2024-05-23; (b) a route coverage profile is produced with limit=1000; "
            "and (c) the authoritative Basic Economy cheapest-by-date for 2024-05-01..2024-05-31 uses price_component='base_fare', considers only operating options "
            "with seats>0 (require_available=True), and resolves ties by lexicographic flight number. If any target is not met, bring it into compliance idempotently "
            "and make no other changes. Return only the minimal verification necessary to substantiate these outcomes."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT096",
                "dates": ["2024-05-23"],
                "status": "available",
                "max_preview": 0
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT296",
                "dates": ["2024-05-23"],
                "status": "available",
                "max_preview": 0
            }),
            Action(name="ListAllFaresByRoute", kwargs={
                "origin": "PHL",
                "destination": "LGA",
                "limit": 1000
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "PHL",
                "destination": "LGA",
                "cabins": ["basic_economy"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number",
                "start_date": "2024-05-01",
                "end_date": "2024-05-31"
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT096",
                "date": "2024-05-23"
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT296",
                "date": "2024-05-23"
            }),

        ],
        outputs=[
        # Route profile (limit check + route echo)
        '"route":"PHL→LGA","limit":1000,"total":60',

        # Operating eligibility on 2024-05-23
        '"date":"2024-05-23","flight_number":"HAT096","flight_status":"available"',
        '"date":"2024-05-23","flight_number":"HAT296","flight_status":"available"',

        '"date":"2024-05-16","basic_economy_price":81.0,"flight_number":"HAT096"',
        '"date":"2024-05-23","basic_economy_price":98.0,"flight_number":"HAT001"',
        '"date":"2024-05-29","basic_economy_price":59.0,"flight_number":"HAT296"',
        '"date":"2024-05-30","basic_economy_price":86.0,"flight_number":"HAT001"'
    ]


    ),
    Task(
        annotator="0",
        user_id="USER_011",
        instruction=(
            "You need a PHL→LGA corridor audit proving deterministic normalization and cheapest-fare reporting. End-state must show: "
            "(a) HAT001 is operating and neutralized at multiplier 1.00 on 2024-05-20 and 2024-05-21; "
            "(b) a corridor fare census with limit=200; and "
            "(c) cheapest-by-date per cabin (basic_economy, economy, business) across full available history using base_fare only, "
            "only operating options with seats>0, and ties broken lexicographically by flight number. "
            "Limit writes strictly to HAT001 and those dates."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-20", "end_date": "2024-05-21",
                "status": "available"
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-20", "end_date": "2024-05-21",
                "multiplier": 1.00
            }),
            Action(name="ListAllFaresByRoute", kwargs={
                "origin": "PHL", "destination": "LGA", "limit": 200
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "PHL", "destination": "LGA",
                "cabins": ["basic_economy", "economy", "business"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number"
            }),
        ],
        outputs=[],  # reporting lives in tools' return; no extra strings needed
    ),
    Task(
        annotator="0",
        user_id="USER_012",
        instruction=(
            "Execute HQ Pricing analysis duties. You were requested to make an audit that confirms HAT300 is normalized to operational compliance "
            "on 2024-05-20, 2024-05-21, and 2024-05-22 with schedule status 'available', aircraft 'A320', and crew "
            "['PIC-7321','SIC-8470','FA-1180'] (idempotent). You also need a per-date MSP→EWR snapshot for the same window, "
            "returning the cheapest Basic Economy option per day using base_fare, restricted to operating flights only "
            "(status 'available' with seats>0) and applying lexicographic flight number as a tie-breaker. "
            "Return only the computed cheapest-by-date list for that window. Scope is limited strictly to HAT300 compliance "
            "and the MSP→EWR corridor in that window."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT300",
                "dates": ["2024-05-20","2024-05-21","2024-05-22"],
                "status": "available",
                "aircraft": "A320",
                "crew": ["PIC-7321","SIC-8470","FA-1180"]
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "MSP",
                "destination": "EWR",
                "cabins": ["basic_economy"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number",
                "start_date": "2024-05-20",
                "end_date": "2024-05-22"
            }),
        ],
        outputs=[
            '"cheapest_by_date": [',
            '{"date": "2024-05-20", "flight_number": "HAT141", "basic_economy_price": 58.0, "price_source": "flights_json"}',
            '{"date": "2024-05-21", "flight_number": "HAT300", "basic_economy_price": 59.0, "price_source": "flights_json"}',
            '{"date": "2024-05-22", "flight_number": "HAT300", "basic_economy_price": 59.0, "price_source": "flights_json"}',
            '"route": {"origin": "MSP", "destination": "EWR"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_013",
        instruction=(
            "Execute on-duty Pricing analysis for the PHL→LGA corridor. You want a baseline and analytics for HAT001 covering "
            "2024-05-20 through 2024-05-22. You need HAT001 normalized so it is sellable (status 'available') on those dates without "
            "changing aircraft or crew. For HAT001 in Economy over the same window, you want the average base_fare computed with the "
            "IQR outlier policy (k=1.5) and min_samples=1. For the PHL→LGA corridor over the same dates, you want the Economy cheapest "
            "option per day using base_fare only, limited to sellable flights (status 'available' with seats>0) and applying "
            "lexicographic flight number as the tie-breaker. Scope is strictly these flights, dates, and metrics; return only the "
            "minimal verification data."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22",
                "status": "available"
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT001",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22",
                "outlier_policy": {"method": "iqr", "k": 1.5},
                "min_samples": 1
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "PHL",
                "destination": "LGA",
                "cabins": ["economy"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_014",
        instruction=(
            "Execute HQ Pricing analysis duties. You want HAT001 (PHL→LGA) sellable and corridor-baselined on 2024-05-21 without any bulk price/seat writes. "
            "End-state: status 'available'; seasonal multiplier 1.00 on base_fare; and exactly — Basic Economy 16 seats at 76, Economy 13 seats at 189, "
            "Business held at 10 seats and 201. Operate strictly on that flight/date and use per-cabin atomic updates only. Return no outputs."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001", "dates": ["2024-05-21"], "status": "available"
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001", "start_date": "2024-05-21", "end_date": "2024-05-21", "multiplier": 1.00
            }),
            # Seats by cabin (atomic)
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "available_seats": {"basic_economy": 16}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "available_seats": {"economy": 13}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "available_seats": {"business": 10}
            }),
            # Prices by cabin (atomic)
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "prices": {"basic_economy": 76}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "prices": {"economy": 189}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "prices": {"business": 201}
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_015",
        instruction=(
            "Execute Pricing analysis duties on duty. You need to verify a Business-cabin base_fare markdown for HAT002 on 2024-05-24, "
            "with taxes/fees unchanged and other cabins unaffected. You want an idempotent 12% markdown applied to Business on that date, "
            "and a readback of the Business fare before and after as old_price and new_price. Capture baseline Business seat availability "
            "and baseline Economy and Basic Economy base_fare levels for context only (no post-change readbacks beyond Business new_price). "
            "Limit scope strictly to HAT002 on 2024-05-24 and return only old_price and new_price."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business"
            }),
            Action(name="GetAvailableSeat", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "cabin": "business"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "basic_economy"
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business", "percent": 12
            }),
        ],
        outputs=[
            '"old_price": 415.0',
            '"new_price": 365.2',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_016",
        instruction=(
            "Execute Pricing analysis duties on duty for HAT003 on 2024-05-28. Objective: produce a controlled +5.50 delta audit for "
            "cabin ∈ {'basic_economy','economy'} with taxes/fees unchanged. Policy constraints: operate on price_component='base_fare' "
            "only; spot-price reads may explicitly use "
            "fallback_to_flights=True if a bucket is not directly readable. Evidence required: Basic Economy before/after values "
            "showing an exact +5.50 increase on 2024-05-28, and Economy before/after values where the pre-change Economy fare is "
            "recorded and then reflects an exact +5.50 increase on 2024-05-28. Scope is strictly flight='HAT003' and date=2024-05-28."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT003",
                "date": "2024-05-28",
                "fare_class": "basic_economy",
                "fallback_to_flights": True
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT003",
                "date": "2024-05-28",
                "fare_class": "basic_economy",
                "delta": 5.50
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT003",
                "date": "2024-05-28",
                "fare_class": "economy",
                "delta": 5.50
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_017",
        instruction=(
            "Execute HQ Pricing analysis duties. You want HAT001 reviewed for operational consistency across 2024-05-20 and 2024-05-22. "
            "Your end state is: on 2024-05-20 the schedule is 'available' and the published prices bucket reflects Economy and Business "
            "both at a base_fare of 189.0 (taxes/fees unchanged); on 2024-05-22 the schedule reflects 'cancelled'. "
            "Scope is strictly HAT001 and only these dates. Return only minimal schedule confirmation."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-20"],
                "status": "available",
                "max_preview": 0
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-20",
                "prices": {"economy": 189.0, "business": 189.0}
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-22"],
                "status": "cancelled",
                "max_preview": 0
            }),
            # Final readback for grounding (covers both dates)
            Action(name="GetFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-20",
                "end_date": "2024-05-22"
            }),
        ],
        outputs=[
            '"flight_number": "HAT001"',
            '"date": "2024-05-20"',
            '"status": "available"',
            '"date": "2024-05-22"',
            '"status": "cancelled"',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction=(
            "You need to set HAT002 operating on 2024-05-28, 2024-05-29, and 2024-05-30; capture baseline spot prices at the exact checkpoints "
            "(HAT002: 2024-05-28 basic_economy, 2024-05-29 economy, 2024-05-30 business) plus a control spot price for HAT001 economy on 2024-05-29; "
            "then apply a uniform base_fare uplift of 1.10 to HAT002 across 2024-05-28..2024-05-30 with a 5-row preview. Taxes/fees unchanged. "
            "Scope is ONLY the flights and dates named."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "dates": ["2024-05-28","2024-05-29","2024-05-30"],
                "status": "available"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-28", "fare_class": "basic_economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-29", "fare_class": "economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-30", "fare_class": "business"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT001", "date": "2024-05-29", "fare_class": "economy"
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-28", "end_date": "2024-05-30",
                "multiplier": 1.10, "max_preview": 5
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_019",
        instruction=(
            "Execute Pricing analysis duties on duty for 2024-05-21. Objective: normalize HAT001 base_fare across cabins "
            "{'business','economy','basic_economy'} using a uniform additive delta of -7.00 (taxes/fees unchanged; scope limited "
            "to flight='HAT001' and date=2024-05-21). Spot-price reads are permitted before adjustment; if a bucket price is not "
            "directly readable, you are explicitly authorized to use fallback to published flight pricing (fallback_to_flights=True)."
        ),
        actions=[
            Action(
                name="AdjustFareClassPricing",
                kwargs={"flight_number": "HAT001", "date": "2024-05-21", "fare_class": "business", "delta": -7.00}
            ),
            Action(
                name="AdjustFareClassPricing",
                kwargs={"flight_number": "HAT001", "date": "2024-05-21", "fare_class": "economy", "delta": -7.00}
            ),
            Action(
                name="AdjustFareClassPricing",
                kwargs={"flight_number": "HAT001", "date": "2024-05-21", "fare_class": "basic_economy", "delta": -7.00}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_020",
        instruction=(
            "Execute +12.00 base_fare delta confirmation for HAT200 on 2024-05-27. For Business, Economy, and Basic Economy, "
            "prove each cabin's base_fare on that date reflects an exact +12.00 increase from its documented 'before' value, with taxes/fees unchanged. "
            "Include the before and after prices so the +12.00 delta is unambiguous per cabin. Limit strictly to HAT200 and 2024-05-27. "
            "Return no free-text."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "business"}),
            Action(name="GetCurrentTicketPrice", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "economy"}),
            Action(name="GetCurrentTicketPrice", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "basic_economy"}),

            Action(name="AdjustFareClassPricing", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "business",       "delta": 12.00}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "economy",       "delta": 12.00}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "basic_economy", "delta": 12.00}),

            Action(name="GetCurrentTicketPrice", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "business"}),
            Action(name="GetCurrentTicketPrice", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "economy"}),
            Action(name="GetCurrentTicketPrice", kwargs={"flight_number": "HAT200", "date": "2024-05-27", "fare_class": "basic_economy"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction=("Execute HQ Pricing management duties. You need a 5% discount and neutral-alignment audit for HAT003 in fare_class 'economy' on 2024-05-29. "
        "Execute readback of the current fare for 2024-05-29, confirmation that a discount of 5% is applied on 2024-05-29, "
        "and confirmation that the seasonal alignment that day is neutral with multiplier=1.00 and a preview of up to 5 examples. "
        "Limit scope strictly to this flight, fare_class, and date, and return only the minimal verification fields."),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT003", "date": "2024-05-29", "fare_class": "economy"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT003", "date": "2024-05-29", "fare_class": "economy", "percent": 5
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT003", "start_date": "2024-05-29", "end_date": "2024-05-29", "multiplier": 1.00, "max_preview": 5
            }),
        ],
        outputs = [
            '"flight_number": "HAT003"',
            '"date": "2024-05-29"',
            '"fare_class": "economy"',
            '"price": 153',
            '"discount_percent": 5.0',
            '"new_price": 145.35',
            '"multiplier": 1.0',
            '"preview": []'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_022",
        instruction=(
            "Execute HQ Pricing management duties. You want to apply a 5% markdown and enforce neutral seasonal alignment (multiplier 1.00) "
            "on HAT003 (Business cabin) for 2024-05-29, then confirm these changes in the audit. "
            "You also want context over 2024-05-27..2024-05-30: the Business base_fare on 2024-05-29, "
            "and window statistics (average, median, count) using the standard IQR outlier policy with k=3.0 and min_samples=1. "
            "Scope is strictly HAT003, fare_class 'business', base_fare only—taxes/fees unchanged. "
            "Return only the requested fields."
        ),
        actions=[
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT003",
                "date": "2024-05-29",
                "fare_class": "business",
                "percent": 5
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT003",
                "fare_class": "business",
                "start_date": "2024-05-29",
                "end_date": "2024-05-29",
                "multiplier": 1.00
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT003",
                "date": "2024-05-29",
                "fare_class": "business"
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT003",
                "fare_class": "business",
                "start_date": "2024-05-27",
                "end_date": "2024-05-30",
                "price_component": "base_fare",
                "outlier_policy": {"method": "iqr", "k": 3.0},
                "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
        ],
        outputs=[
            '"flight_number": "HAT003"',
            '"date": "2024-05-29"',
            '"fare_class": "business"',
            '"price": 224.2',

            '"average_price": 373.05',
            '"median_price": 414.5',
            '"sample_size": 4',

            '"discount_percent": 5.0',
            '"new_price": 224.2',
            '"multiplier": 1.0'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_023",
        instruction=(
            "Execute HQ Pricing management duties. Objective: validate discounting and seasonal-normalization for HAT003 in cabin 'basic_economy' on 2024-05-29, "
            "and provide supporting window statistics.\n"
            "Policy constraints: discount=5% on base_fare for 2024-05-29; seasonal normalization multiplier=1.00 on 2024-05-29 with max_preview=5; "
            "window stats for 2024-05-27..2024-05-30 on base_fare with min_samples=1 reporting average, median, and count. "
            "Evidence must appear in this order: pre-change spot price, window stats, discount applied, seasonal normalization preview, post-change spot price. "
            "Scope limited to HAT003 and the stated dates/cabin."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT003", "date": "2024-05-29", "fare_class": "basic_economy"
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT003", "fare_class": "basic_economy",
                "start_date": "2024-05-27", "end_date": "2024-05-30",
                "price_component": "base_fare", "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT003", "date": "2024-05-29", "fare_class": "basic_economy", "percent": 5
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT003",
                "start_date": "2024-05-29", "end_date": "2024-05-29",
                "multiplier": 1.00, "max_preview": 5
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT003", "date": "2024-05-29", "fare_class": "basic_economy"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_024",
        instruction=(
            "Execute HQ Pricing analysis duties. You want to apply a composite base_fare adjustment to specific "
            "HAT001 and HAT002 flight/date/fare_class pairs during May. The composite policy is A(p) = (p × 0.97) + 2.00 "
            "and needs to be realized as an ordered two-step write for each pair: first apply a 3% markdown using "
            "apply_discount_to_flight, then add +2.00 using adjust_fare_class_pricing. Do not substitute a single "
            "composite write or any alternative method. Seats, other cabins, taxes, and fees remain unchanged. "
            "Scope is limited strictly to HAT001 on 2024-05-21 basic_economy, 2024-05-22 economy, 2024-05-28 business; "
            "and HAT002 on 2024-05-29 basic_economy, 2024-05-30 economy, 2024-05-20 business. "
            "Return only the adjusted verification values for these six pairs."
        ),
        actions=[
            # HAT001
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "fare_class": "basic_economy", "percent": 3
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "fare_class": "basic_economy", "delta": 2.0
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "fare_class": "basic_economy"
            }),

            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT001", "date": "2024-05-22", "fare_class": "economy", "percent": 3
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT001", "date": "2024-05-22", "fare_class": "economy", "delta": 2.0
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT001", "date": "2024-05-22", "fare_class": "economy"
            }),

            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT001", "date": "2024-05-28", "fare_class": "business", "percent": 3
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT001", "date": "2024-05-28", "fare_class": "business", "delta": 2.0
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT001", "date": "2024-05-28", "fare_class": "business"
            }),

            # HAT002
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-29", "fare_class": "basic_economy", "percent": 3
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT002", "date": "2024-05-29", "fare_class": "basic_economy", "delta": 2.0
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-29", "fare_class": "basic_economy"
            }),

            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-30", "fare_class": "economy", "percent": 3
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT002", "date": "2024-05-30", "fare_class": "economy", "delta": 2.0
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-30", "fare_class": "economy"
            }),

            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-20", "fare_class": "business", "percent": 3
            }),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT002", "date": "2024-05-20", "fare_class": "business", "delta": 2.0
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-20", "fare_class": "business"
            }),
        ],
        outputs=[
            '"flight_number": "HAT001", "date": "2024-05-21", "fare_class": "basic_economy", "adjusted_price": 81.54',
            '"flight_number": "HAT001", "date": "2024-05-22", "fare_class": "economy", "adjusted_price": 118.40',
            '"flight_number": "HAT001", "date": "2024-05-28", "fare_class": "business", "adjusted_price": 200.85',
            '"flight_number": "HAT002", "date": "2024-05-29", "fare_class": "basic_economy", "adjusted_price": 75.72',
            '"flight_number": "HAT002", "date": "2024-05-30", "fare_class": "economy", "adjusted_price": 139.74',
            '"flight_number": "HAT002", "date": "2024-05-20", "fare_class": "business", "adjusted_price": 335.68',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction=(
            "Execute HQ Pricing analysis duties. Apply chained base_fare updates for the listed flight/date/cabin pairs "
            "using exactly percent=3 followed by delta=-15.0. Pairs: HAT003 — 2024-05-21 basic_economy; 2024-05-22 economy; "
            "2024-05-28 business. HAT004 — 2024-05-29 basic_economy; 2024-05-30 economy; 2024-05-20 business. "
            "HAT005 — 2024-05-21 basic_economy; 2024-05-22 economy; 2024-05-28 business. Do not modify other cabins, seats, "
            "taxes, or fees. No readbacks or outputs are required."
        ),
        actions=[
            # HAT003
            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT003","date":"2024-05-21","fare_class":"basic_economy","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT003","date":"2024-05-21","fare_class":"basic_economy","delta":-15.0}),

            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT003","date":"2024-05-22","fare_class":"economy","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT003","date":"2024-05-22","fare_class":"economy","delta":-15.0}),

            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT003","date":"2024-05-28","fare_class":"business","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT003","date":"2024-05-28","fare_class":"business","delta":-15.0}),

            # HAT004
            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT004","date":"2024-05-29","fare_class":"basic_economy","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT004","date":"2024-05-29","fare_class":"basic_economy","delta":-15.0}),

            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT004","date":"2024-05-30","fare_class":"economy","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT004","date":"2024-05-30","fare_class":"economy","delta":-15.0}),

            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT004","date":"2024-05-20","fare_class":"business","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT004","date":"2024-05-20","fare_class":"business","delta":-15.0}),

            # HAT005
            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT005","date":"2024-05-21","fare_class":"basic_economy","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT005","date":"2024-05-21","fare_class":"basic_economy","delta":-15.0}),

            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT005","date":"2024-05-22","fare_class":"economy","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT005","date":"2024-05-22","fare_class":"economy","delta":-15.0}),

            Action(name="ApplyDiscountToFlight", kwargs={"flight_number":"HAT005","date":"2024-05-28","fare_class":"business","percent":3}),
            Action(name="AdjustFareClassPricing", kwargs={"flight_number":"HAT005","date":"2024-05-28","fare_class":"business","delta":-15.0}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_026",
        instruction=(
            "Execute HQ Pricing analysis duties. You want a cross-flight pricing dossier for HAT111 and HAT001 that proves all of the following end-states:\n"
            "• For HAT111 on 2024-05-21: Economy coverage is evidenced by a readable, authoritative bucket price snapshot.\n"
            "• For HAT001 on 2024-05-21: Economy base_fare is normalized to exactly 134.42; this normalization must ignore operating status by using the field require_available=false on the pricing write, so it applies deterministically whether or not the date is currently 'available'.\n"
            "• A point-in-time snapshot is captured for HAT111 Economy on 2024-05-20.\n"
            "• For HAT111 on 2024-05-17: schedule is operating (status 'available') and Economy reflects exactly 13 seats at 189 (idempotent; other cabins unchanged).\n"
            "Scope is strictly these flights and dates; policy applies for determinism and idempotency."
        ),
        actions=[
            # HAT111 snapshot on 2024-05-21
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT111", "date": "2024-05-21", "fare_class": "economy"
            }),

            # HAT001 normalization write + read-after-write
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21",
                "fare_class": "economy", "price": 134.42,
                "require_available": False
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "fare_class": "economy"
            }),

            # HAT111 point-in-time snapshot on 2024-05-20
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT111", "date": "2024-05-20", "fare_class": "economy"
            }),

            # HAT111 enforce schedule + read-after-write
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT111", "dates": ["2024-05-17"], "status": "available"
            }),
            Action(name="GetFlightSchedule", kwargs={
                "flight_number": "HAT111", "start_date": "2024-05-17", "end_date": "2024-05-17"
            }),

            # HAT111 enforce economy seats/prices + read-after-write
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT111", "date": "2024-05-17",
                "available_seats": {"economy": 13},
                "prices": {"economy": 189}
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT111", "date": "2024-05-17", "fare_class": "economy"
            }),
        ],
        outputs=[
            '"HAT111_2024-05-21_economy_price": 109',
            '"HAT001_2024-05-21_economy_price": 118',
            '"HAT111_2024-05-20_economy_price": 144',
            '"HAT111_2024-05-17_status": "available"',
            '"HAT111_2024-05-17_economy_seats": 13',
            '"HAT111_2024-05-17_economy_price": 189'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_027",
        instruction=(
            "Generate corridor snapshot bundling three spot-checks with a uniform seasonal alignment, while guaranteeing HAT004 remains untouched.\n\n"
            "Deliverables:\n"
            "• Spot-check base_fare for: HAT001 (economy) on 2024-05-21; HAT002 (business) on 2024-05-29; HAT003 (basic_economy) on 2024-05-25.\n"
            "• Ensure HAT001, HAT002, and HAT003 are sellable across 2024-05-20..2024-05-30 (status 'available'; aircraft/crew unchanged); changes must be idempotent.\n"
            "• Apply a uniform 1.05 uplift to base_fare for those same three flights over that window; taxes/fees unchanged.\n\n"
            "Scope is strictly the flights and dates specified; HAT004 must remain unchanged (no reads or writes to HAT004)."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001", "start_date": "2024-05-20", "end_date": "2024-05-30", "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002", "start_date": "2024-05-20", "end_date": "2024-05-30", "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT003", "start_date": "2024-05-20", "end_date": "2024-05-30", "status": "available"
            }),

            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT001", "date": "2024-05-21", "fare_class": "economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-29", "fare_class": "business"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT003", "date": "2024-05-25", "fare_class": "basic_economy"
            }),

            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001", "start_date": "2024-05-20", "end_date": "2024-05-30", "multiplier": 1.05
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT002", "start_date": "2024-05-20", "end_date": "2024-05-30", "multiplier": 1.05
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT003", "start_date": "2024-05-20", "end_date": "2024-05-30", "multiplier": 1.05
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction=(
            "Execute HQ Pricing analysis duties. You want to normalize the following flights by date, using the exact values below, "
            "and make only idempotent changes (no change where values already match). Bring each flight into compliance such that "
            "the schedule is operating (status 'available'), published base_fare buckets equal the specified prices, and seat counts "
            "equal the specified values.\n"
            "• For HAT112 on 2024-05-02: available_seats = {'basic_economy': 16, 'economy': 13, 'business': 9} and "
            "  prices = {'basic_economy': 76, 'economy': 189, 'business': 498}.\n"
            "• For HAT114 on 2024-05-06: available_seats = {'basic_economy': 16, 'economy': 13, 'business': 9} and "
            "  prices = {'basic_economy': 76, 'economy': 189, 'business': 498}.\n"
            "• For HAT115 on 2024-05-06: available_seats = {'basic_economy': 16, 'economy': 13, 'business': 9} and "
            "  prices = {'basic_economy': 76, 'economy': 189, 'business': 498}.\n"
            "Update only these dates and fields; do not modify other cabins, taxes, or fees."
        ),
        actions=[
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT112",
                "date": "2024-05-02",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT114",
                "date": "2024-05-06",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT115",
                "date": "2024-05-06",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_029",
        instruction=(
            "Execute HQ Pricing analysis duties. For HAT001, HAT002, and HAT003 across 2024-05-20..2024-05-30, "
            "set schedule status='available' on all dates (no preview). Apply a seasonal base-fare uplift with "
            "multiplier=1.05 to **Economy only** over the same window for each flight, with max_preview=5. "
            "Do not modify Basic Economy or Business, taxes, fees, or seats. Final-state requirement: "
            "HAT002 on 2024-05-25 must be 'cancelled' (temporary 'available' for normalization is acceptable). "
            "Limit scope strictly to these flights and dates."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "status": "available", "max_preview": 0
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "status": "available", "max_preview": 0
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT003", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "status": "available", "max_preview": 0
            }),
            # Economy-only seasonal uplift (agents often uplift all cabins)
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "multiplier": 1.05, "max_preview": 5, "fare_class": "economy"
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT002", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "multiplier": 1.05, "max_preview": 5, "fare_class": "economy"
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT003", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "multiplier": 1.05, "max_preview": 5, "fare_class": "economy"
            }),
            # Required final-state revert (agents often forget)
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002", "dates": ["2024-05-25"], "status": "cancelled", "max_preview": 0
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction=(
            "Execute HQ Pricing analysis duties. For HAT001 and HAT002 across 2024-05-20..2024-05-30, set schedule status='available' "
            "on all dates (no change if already). Apply a seasonal base-fare uplift with multiplier=1.05 to **HAT001 economy only** "
            "(do not modify HAT001 basic_economy or business) and to **all cabins on HAT002**. **HAT003 is frozen and must remain "
            "unchanged.** Final-state requirement: **HAT002 on 2024-05-27 is 'cancelled'** after all checks. Taxes/fees and seats stay "
            "unchanged; scope is strictly these flights and dates."
        ),
        actions=[
            # publish window (idempotent)
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001", "start_date": "2024-05-20", "end_date": "2024-05-30", "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002", "start_date": "2024-05-20", "end_date": "2024-05-30", "status": "available"
            }),
            # Tripwire A: per-cabin atomic seasonal on HAT001 (economy only)
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "multiplier": 1.05, "fare_class": "economy"
            }),
            # Tripwire B: all-cabins seasonal on HAT002 (no fare_class filter)
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT002", "start_date": "2024-05-20", "end_date": "2024-05-30",
                "multiplier": 1.05
            }),
            # HAT003 intentionally untouched (frozen)
            # Tripwire C: single-date re-cancel (agents often forget)
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002", "dates": ["2024-05-27"], "status": "cancelled"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_031",
        instruction=(
            "Execute HQ Pricing analysis duties. Produce a Business-fare discount cycle audit for HAT002 on 2024-05-24. "
            "The audit must report: (1) the Business fare before adjustment as price_before; (2) the Business fare after "
            "applying discount percent=12 on 2024-05-24 as price_after_discount; and (3) the restored Business fare after "
            "removing discount percent=12 on 2024-05-24 as price_after_revert. Do not modify other cabins, dates, taxes, or fees. "
            "Return only price_before, price_after_discount, and price_after_revert."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business", "percent": 12
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business"
            }),
            Action(name="RemoveDiscountFromFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business", "percent": 12
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business"
            }),
        ],
        outputs=[
            '"price_before": 415',
            '"price_after_discount": 365.2',
            '"price_after_revert": 415.0',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_032",
        instruction=(
            "Execute HQ Pricing analysis duties. Conduct a discount reversibility audit for HAT002 (Business) on 2024-05-24. "
            "The audit must establish: (1) the Business base_fare level on 2024-05-24; (2) the effect of a temporary 12% "
            "markdown; and (3) exact restoration to the original amount using the discount audit trail with the strict mode "
            "token 'strict'. Scope is strictly this flight, this date, and fare_class 'business'."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business", "percent": 12
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business"
            }),
            Action(name="RemoveDiscountFromFlight", kwargs={
                "flight_number": "HAT002", "date": "2024-05-24", "fare_class": "business", "percent": 12, "strict": True
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction=(
            "Execute HQ Pricing analysis duties. You want a point-in-time reversibility audit for HAT080 (Business) on 2024-05-19. "
            "You need to verify that a 15% markdown on base_fare is fully reversible on that date and that the ending base_fare "
            "exactly matches the original amount (no net change). The revert must use the strict revert policy ('strict'). "
            "Scope is strictly HAT080, 2024-05-19, fare_class 'business'; base_fare only—taxes/fees unchanged; changes must be idempotent."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT080",
                "date": "2024-05-19",
                "fare_class": "business"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT080",
                "date": "2024-05-19",
                "fare_class": "business",
                "percent": 15
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT080",
                "date": "2024-05-19",
                "fare_class": "business"
            }),
            Action(name="RemoveDiscountFromFlight", kwargs={
                "flight_number": "HAT080",
                "date": "2024-05-19",
                "fare_class": "business",
                "strict": True
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction=(
            "Execute Ops HQ duties. You want flight HAT014 on 2024-05-05 to be available with "
            "available_seats={'basic_economy': 16, 'economy': 13, 'business': 9} and "
            "prices={'basic_economy': 76, 'economy': 189, 'business': 498}; and you want it assigned to aircraft_id 'AC007'. "
            "You also want confirmation that the aircraft with tail_number 'PR-YJB' exists in the fleet registry (read-only check). "
            "Limit scope strictly to HAT014 on 2024-05-05; make any changes idempotent."
        ),
        actions=[

            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT014",
                "date": "2024-05-05",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
            Action(
                name="GetAircraftByTailNumber",
                kwargs={"tail_number": "PR-YJB"}
            ),
            Action(
                name="AssignAircraftToFlight",
                kwargs={
                    "flight_number": "HAT014",
                    "date": "2024-05-05",
                    "new_aircraft_id": "AC007"
                }
            ),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_035",
        instruction=(
            "Execute HQ duty analysis tasks. Normalize HAT003 across 2024-05-22..2024-05-26. Final state: schedule status is "
            "'cancelled' on 2024-05-22 and 2024-05-23; a no-charge upgrade path from 'basic_economy' to 'economy' is active "
            "for 2024-05-24..2024-05-26; and a seasonal pricing uplift with multiplier 1.02 is applied over 2024-05-24..2024-05-26 "
            "with a preview limited to 5 rows (max_preview=5). Scope is strictly HAT003 and these dates; base_fare only—taxes/fees "
            "unchanged; changes must be idempotent."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT003",
                "dates": ["2024-05-22", "2024-05-23"],
                "status": "cancelled"
            }),
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT003",
                "start_date": "2024-05-24",
                "end_date": "2024-05-26",
                "from_cabin": "basic_economy",
                "to_cabin": "economy",
                "no_charge": True
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT003",
                "start_date": "2024-05-24",
                "end_date": "2024-05-26",
                "multiplier": 1.02,
                "max_preview": 5
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction=(
            "Execute Ops HQ duties. You want an operational adjustment for HAT270 across 2024-05-23 through 2024-05-25. "
            "Your goals are: the schedule is published as 'available' on these dates, Economy on 2024-05-24 reflects "
            "a normalized base_fare of 280.00, and Economy-to-Business upgrades are available at no charge over the "
            "same window. Scope is strictly HAT270; other cabins, aircraft, crew, taxes, and fees remain unchanged. "
            "Return only minimal confirmation of these outcomes."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT270",
                "dates": ["2024-05-23", "2024-05-24", "2024-05-25"],
                "status": "available"
            }),
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT270",
                "start_date": "2024-05-23",
                "end_date": "2024-05-25",
                "from_cabin": "economy",
                "to_cabin": "business",
                "no_charge": True
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT270",
                "date": "2024-05-24",
                "fare_class": "economy",
                "price": 280.00,
                "require_available": True
            }),
            # Verification: confirm schedule is available
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT270",
                "date": "2024-05-24"
            }),
        ],
        outputs=[
            '"flight_number": "HAT270"',
            '"date": "2024-05-24"',
            '"status": "available"',
            '"fare_class": "economy"',
            '"price": 280.00',
            '"from_cabin": "economy"',
            '"to_cabin": "business"',
            '"no_charge": true'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction=(
            "You need a seasonal down-adjustment audit for HAT001 (economy) covering 2024-05-20..2024-05-30. "
            "You require economy price history for that exact window included for context without modification "
            "(use operating options only), then you must have a seasonal normalization applied only to the economy cabin "
            "over the same window reflecting a 0.95 multiplier with a preview limited to five examples. "
            "After normalization, you require window statistics on base_fare reported using the standard outlier policy "
            "(IQR k=1.5) with min_samples=1, and you want median and sample size included. "
            "Scope is confined to this flight and window ONLY; output is limited to the named structured fields."
        ),
        actions=[
            # Context-only read (explicit window + availability)
            Action(name="GetHistoricalTicketPrices", kwargs={
                "flight_number": "HAT001",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date": "2024-05-30",
                "require_available": True
            }),
            # Write: apply seasonal normalization (economy only)
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date": "2024-05-30",
                "multiplier": 0.95,
                "max_preview": 5
            }),
            # Post-write readback for verification (explicitly post-normalization)
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT001",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date": "2024-05-30",
                "price_component": "base_fare",
                "outlier_policy": {"method": "iqr", "k": 1.5},
                "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
        ],
        outputs=[
            '"flight_number": "HAT001"',
            '"fare_class": "economy"',
            '"start_date": "2024-05-20"',
            '"end_date": "2024-05-30"',

            # Window statistics (post-adjustment values—numbers from your run)
            '"average_price": 137.66',
            '"median_price": 134.9',
            '"sample_size": 11',

            # Seasonal normalization preview anchors (economy-only; 5 examples)
            '"date": "2024-05-20"', '"old": 137.0', '"new": 130.15',
            '"date": "2024-05-21"', '"old": 118.0', '"new": 112.1',
            '"date": "2024-05-22"', '"old": 120.0', '"new": 114.0',
            '"date": "2024-05-23"', '"old": 103.0', '"new": 97.85',
            '"date": "2024-05-24"', '"old": 176.0', '"new": 167.2',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_038",
        instruction=(
            "Execute Pricing HQ duties. You want to normalize HAT010 for 2024-05-13..2024-05-15. "
            "Your final state is: schedule status is 'available' on 2024-05-13, 2024-05-14, and 2024-05-15; "
            "for 2024-05-13 the published prices bucket and inventory reflect exactly "
            "available_seats={'basic_economy': 16, 'economy': 13, 'business': 5} and "
            "prices={'basic_economy': 101, 'economy': 200, 'business': 500}; "
            "for 2024-05-14 and 2024-05-15 you do not alter inventory or prices (status only). "
            "All changes must be idempotent and limited strictly to this flight and these dates. "
            "This task produces no return payload at all."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT010",
                "dates": ["2024-05-13", "2024-05-14", "2024-05-15"],
                "status": "available"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT010",
                "date": "2024-05-13",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 5},
                "prices": {"basic_economy": 101, "economy": 200, "business": 500}
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_039",
        instruction=(
            "You need HAT003 with schedule status 'available' on 2024-05-24. "
            "You need Basic Economy window statistics across 2024-05-20..2024-05-30, "
            "calculated on base_fare with the standard IQR outlier policy (k=1.5), requiring at least one valid sample, "
            "and including median and sample size. "
            "The confirmed metrics for this window are average_price 82.09, median_price 88.0, and sample_size 11. "
            "This normalization step is internal; do NOT return additional outputs."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT003",
                "dates": ["2024-05-24"],
                "status": "available"
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT003",
                "fare_class": "basic_economy",
                "start_date": "2024-05-20",
                "end_date": "2024-05-30",
                "outlier_policy": {"method": "iqr", "k": 1.5},
                "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
        ],
        outputs=[
            '"average_price": 82.09"',
            '"median_price": 88.0"',
            '"sample_size": 11"',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_040",
        instruction=(
            "Execute Pricing analysis duties at HQ. You want a coverage profile for MSP→EWR with a high listing limit "
            "(1000), and you want the authoritative Basic Economy cheapest-by-date across 2024-05-23..2024-05-30 using "
            "base fare only and considering only operating options, with tie-breaks handled per policy. You also want "
            "flight HAT300 marked cancelled on 2024-05-11 and 2024-05-23. Limit scope strictly to this route and these "
            "dates; make any changes idempotent."
        ),
        actions=[
            Action(name="ListAllFaresByRoute", kwargs={
                "origin": "MSP",
                "destination": "EWR",
                "limit": 1000
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "MSP",
                "destination": "EWR",
                "cabins": ["basic_economy"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number",
                "start_date": "2024-05-23",
                "end_date": "2024-05-30"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT300",
                "dates": ["2024-05-11", "2024-05-23"],
                "status": "cancelled"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_041",
        instruction=(
            "Execute Pricing HQ duties. Deliver an Economy-cabin audit and normalization packet for HAT300. "
            "Include: (1) the Economy price time series over the full available history (no date filter); "
            "(2) window statistics for 2024-05-20..2024-05-22 on price_component 'base_fare', reporting average, median, "
            "and sample size; (3) the Economy price-change audit trail for that window; (4) the current Economy fare on "
            "2024-05-20; and (5) a committed normalization for 2024-05-20 setting available_seats={'economy': 20} and "
            "prices={'economy': 230.0}. Ensure the final state for 2024-05-20 reflects that normalization. "
            "Scope is strictly HAT300, fare_class 'economy', and these dates; base_fare only—taxes/fees unchanged."
        ),
        actions=[
            Action(name="GetHistoricalTicketPrices", kwargs={
                "flight_number": "HAT300",
                "fare_class": "economy"
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT300",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22",
                "price_component": "base_fare",
                "include": {"median": True, "count": True}
            }),
            Action(name="GetPriceChangeHistory", kwargs={
                "flight_number": "HAT300",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT300",
                "date": "2024-05-20",
                "available_seats": {"economy": 20},
                "prices": {"economy": 230.0}
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction=(
            "Execute HQ Pricing analysis duties. You need an authoritative per-cabin cheapest-by-date audit for PHL→LGA across the full "
            "available history, with per-cabin reports for ['basic_economy','economy','business'] on price_component 'base_fare', "
            "limited to operating options (status='available', seats>0) and tie-breaker lexicographic flight number. "
            "You also want HAT001 price-change histories for fare_class 'business' and 'economy' for 2024-05-20..2024-05-30. "
            "For evidence, record a seasonal normalization on HAT001 **economy only** at multiplier=1.00 on 2024-05-21 "
            "(no other cabins). Final-state requirements for HAT001 on 2024-05-21: status 'cancelled' and aircraft 'AC008' "
            "on the flight-date. A temporary normalization to 'available' solely to ensure coverage is acceptable. "
            "Return only the requested fields."
        ),
        actions=[
            # temporary normalization for coverage (gate for price ops)
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-21",
                "end_date":   "2024-05-21",
                "status": "available"
            }),

            # TRIPWIRE: neutral seasonal write (economy only) creates an audit row most agents omit
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-21",
                "end_date":   "2024-05-21",
                "multiplier": 1.00,
                "fare_class": "economy"
            }),

            # reads for the audit
            Action(name="GetPriceChangeHistory", kwargs={
                "flight_number": "HAT001",
                "fare_class": "business",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-30"
            }),
            Action(name="GetPriceChangeHistory", kwargs={
                "flight_number": "HAT001",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-30"
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "PHL",
                "destination": "LGA",
                "cabins": ["basic_economy"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number"
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "PHL",
                "destination": "LGA",
                "cabins": ["economy"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number"
            }),
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "PHL",
                "destination": "LGA",
                "cabins": ["business"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number"
            }),

            # final-state: cancelled + explicit aircraft retained on that date
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-21"],
                "status": "cancelled",
                "aircraft": "AC008"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_043",
        instruction=(
            "You require anavailability-normalization and fleet-assignment audit for HAT001, "
            "covering May 20 and May 27, 2024, with a schedule snapshot for May 20–30, 2024. "
            "You need HAT001 marked as 'available' on 2024-05-20 and 2024-05-27, "
            "a schedule snapshot over 2024-05-20..2024-05-30 with explicit confirmation on 2024-05-27, "
            "aircraft context for tail_number 'PP-PTM' normalized to canonical status enums, "
            "and HAT001 on 2024-05-27 assigned to aircraft_id 'AC008'. "
            "Scope is limited ONLY to these entities and dates; return only minimal verification data."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-20", "2024-05-27"],
                "status": "available"
            }),
            Action(name="GetFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-20",
                "end_date": "2024-05-30"
            }),
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-27"
            }),
            # Removed the pre-update aircraft
            Action(name="UpdateAircraftStatus", kwargs={
                "tail_number": "PP-PTM",
                "status": "stored"
            }),
            # Post-update readback to capture normalized lowercase status
            Action(name="GetAircraftByTailNumber", kwargs={
                "tail_number": "PP-PTM"
            }),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-27",
                "new_aircraft_id": "AC008"
            }),
        ],
        outputs=[
            # Schedule confirmations
            '"flight_number": "HAT001"', '"date": "2024-05-20"', '"status": "available"',
            '"flight_number": "HAT001"', '"date": "2024-05-27"', '"status": "available"',

            # Snapshot readback
            '"flight_number": "HAT001"', '"date": "2024-05-27"', '"flight_status": "available"',

            # Aircraft context (from post-update read, normalized to lowercase)
            '"tail_number": "PP-PTM"', '"aircraft_id": "AC008"', '"status": "stored"',

            # Assignment confirmation
            '"flight_number": "HAT001"', '"date": "2024-05-27"', '"new_aircraft_id": "AC008"', '"status": "success"',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction=(
            "Execute HQ Pricing analysis duties. You want HAT001 (Economy) normalized for 2024-05-20 and 2024-05-21, "
            "with base_fare set to 137.00 on 2024-05-20 and 118.00 on 2024-05-21. After this alignment, "
            "you need the Economy window average for 2024-05-20 through 2024-05-21 using the standard IQR outlier policy (k=1.5). "
            "Return exactly three fields: price_2024_05_20, price_2024_05_21, and average_price. "
            "Scope is strictly HAT001 and those dates, and base_fare only—taxes and fees remain unchanged."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-20","2024-05-21"],
                "status": "available"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-20",
                "prices": {"economy": 137.00}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-21",
                "prices": {"economy": 118.00}
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT001",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date": "2024-05-21",
                "price_component": "base_fare",
                "outlier_policy": {"method": "iqr", "k": 1.5},
                "min_samples": 1
            }),
        ],
        outputs=[
            '"price_2024_05_20": 137.00',
            '"price_2024_05_21": 118.00',
            '"average_price": 127.50',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_045",
        instruction=(
            "Generate Business-cabin pricing brief for HAT002 covering 2024-05-23..2024-05-29. "
            "You need the seasonal baseline reflected with a +3% multiplier (1.03) applied in that window, affecting base_fare only while "
            "leaving taxes and fees unchanged, with no preview returned. You want window statistics for the business fare_class in that "
            "window — average_price, median_price, and sample_size — and you want the Business price-change history across the same window. "
            "Scope is confined strictly to this flight and window; output is limited to the named structured fields."
        ),
        actions=[
            # Write confined to the window and to Business only
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-23",
                "end_date": "2024-05-29",
                "multiplier": 1.03,
                "max_preview": 0,
                "fare_class": "business"
            }),
            # Window statistics for Business
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT002",
                "fare_class": "business",
                "start_date": "2024-05-23",
                "end_date": "2024-05-29",
                "price_component": "base_fare",
                "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
            # Business price-change history for the same window
            Action(name="GetPriceChangeHistory", kwargs={
                "flight_number": "HAT002",
                "fare_class": "business",
                "start_date": "2024-05-23",
                "end_date": "2024-05-29"
            }),
        ],
        outputs=[
            # Scope anchors from READ action (Action 2 output)
            '"flight_number": "HAT002"',
            '"fare_class": "business"',
            '"start_date": "2024-05-23"',
            '"end_date": "2024-05-29"',

            # Stats from READ action (Action 2 output, per your log)
            '"average_price": 361.68"',
            '"median_price": 354.32"',
            '"sample_size": 7"',

            # Price-change history from READ action (Action 3 output)
            '"date": "2024-05-23"', '"price": 381.1"',
            '"date": "2024-05-24"', '"price": 427.45"',
            '"date": "2024-05-25"', '"price": 307.97"',
            '"date": "2024-05-26"', '"price": 299.73"',
            '"date": "2024-05-27"', '"price": 247.2"',
            '"date": "2024-05-28"', '"price": 513.97"',
            '"date": "2024-05-29"', '"price": 354.32"',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction=(
            "Execute Pricing HQ duties. You want a PHL→LGA corridor snapshot focused on HAT001 for 2024-05-21. "
            "Your goals are: a cheapest-by-date report for 2024-05-20..2024-05-21 that considers only the Basic Economy cabin, "
            "evaluates on base_fare, restricts to sellable options (status 'available' with seats>0), and resolves ties by the token "
            "'lexicographic_flight_number'; and HAT001 on 2024-05-21 has Economy published at a base_fare of 99.00 in an idempotent way. "
            "Scope is strictly the PHL→LGA corridor and HAT001 on 2024-05-21; base_fare only—taxes/fees unchanged. "
            "Return only minimal confirmation of the corridor parameters and the 2024-05-21 HAT001 price target."
        ),
        actions=[
            # Cheapest-by-date report over the requested window
            Action(name="ComputeCheapestByDateForRoute", kwargs={
                "origin": "PHL",
                "destination": "LGA",
                "cabins": ["basic_economy"],
                "price_component": "base_fare",
                "require_available": True,
                "tie_breaker": "lexicographic_flight_number",
                "start_date": "2024-05-20",
                "end_date": "2024-05-21"
            }),

            # Final deterministic write (price target publish)
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-21"],
                "status": "available",
                "max_preview": 0
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-21",
                "fare_class": "economy",
                "price": 99.00,
                "require_available": True
            }),
        ],
        outputs = [
            '"origin": "PHL"',
            '"destination": "LGA"',
            '"flight_number": "HAT001"',
            '"date": "2024-05-21"',
            '"fare_class": "economy"',
            '"price": 99.0"',
            '"status": "available"',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction="Execute Ops HQ duties. For HAT223: list operational events of types ['cancellation','diversion'] over 2024-05-05..2024-05-25 for context; retrieve the Business fare history; set schedule status='available' on 2024-05-23 and 2024-05-24 (no change if already). Do not modify other dates, aircraft, crew, or cabins.",
        actions=[

            Action(name="GetOperationalEvents", kwargs={
                "flight_number": "HAT223",
                "start_date": "2024-05-05",
                "end_date": "2024-05-25",
                "types": ["cancellation", "diversion"]
            }),
            Action(name="GetHistoricalTicketPrices", kwargs={
                "flight_number": "HAT223",
                "fare_class": "business"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT223",
                "dates": ["2024-05-23", "2024-05-24"],
                "status": "available"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction=(
            "Execute Ops HQ duties. You want HAT223 sellable on 2024-05-23, 2024-05-24, and 2024-05-25 by publishing those dates "
            "(status 'available') without altering aircraft or crew. Over the same window, you want a no-charge upgrade policy in effect "
            "from basic_economy to economy. Finally, for 2024-05-24 you need the Economy base_fare to be exactly 255.00 in the "
            "canonical published prices bucket for that flight-date.\n\n"
            "Constraints and prohibitions (strict):\n"
            "• Write only to the canonical prices bucket (flights[].dates[day].prices). Do not write any legacy inventory price fields.\n"
            "• Do not call set_ticket_price and do not read legacy inventory pricing; ignore any read where price_source != 'canonical'.\n"
            "• Do not modify other cabins, seats, taxes, or fees. Changes must be deterministic and idempotent.\n"
            "• Return only minimal verification."
        ),
        actions=[
            # Publish required dates (publish-before-writes)
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT223",
                "dates": ["2024-05-23", "2024-05-24", "2024-05-25"],
                "status": "available"
            }),
            # Enforce no-charge upgrade mapping over the window
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT223",
                "start_date": "2024-05-23",
                "end_date": "2024-05-25",
                "from_cabin": "basic_economy",
                "to_cabin": "economy",
                "no_charge": True
            }),
            # Canonical price write (economy only) — no legacy/inventory writes
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT223",
                "date": "2024-05-24",
                "prices": {"economy": 255.00}
            }),
            # Canonical readback for audit (must report price_source='canonical')
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT223",
                "date": "2024-05-24",
                "fare_class": "economy"
            }),
        ],
        outputs=[
            '"flight_number":"HAT223"',
            '"status":"available"',
            '"date":"2024-05-24"',
            '"fare_class":"economy"',
            '"price":255.0',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_049",
        instruction=(
            "Execute normalization for HAT002 for the window 2024-05-23 through 2024-05-25. "
            "Ensure that the schedule is operating (status set to 'available') for all dates in that range. "
            "Then, apply a no-charge upgrade across the same window by aligning the Economy base_fare to match "
            "the Basic Economy base_fare. Scope is strictly HAT002 and those dates only; no other corridor work "
            "should be performed. All changes must be idempotent. Do not return any output."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-23",
                "end_date": "2024-05-25",
                "status": "available",
            }),
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-23",
                "end_date": "2024-05-25",
                "from_cabin": "basic_economy",
                "to_cabin": "economy"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction=(
            "Execute Pricing HQ analyst. You want a Business-cabin audit and single-day normalization for HAT300. "
            "Scope is strictly HAT300 and the dates 2024-05-20..2024-05-22, fare_class 'business', base_fare only—taxes/fees unchanged. "
            "Generate Business base_fare time series over the full available history, window statistics for 2024-05-20..2024-05-22 "
            "with min_samples=1 (including median and sample size), and then a deterministic normalization on 2024-05-20 "
            "that leaves exactly available_seats.business=9 and prices.business=498. "
            "Writes must be idempotent and confined to these dates. "
            "This task produces no return payload at all."
        ),
        actions=[
            Action(name="GetHistoricalTicketPrices", kwargs={
                "flight_number": "HAT300",
                "fare_class": "business"
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT300",
                "fare_class": "business",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22",
                "price_component": "base_fare",
                "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT300",
                "date": "2024-05-20",
                "available_seats": {"business": 9},
                "prices": {"business": 498}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction=(
            "Execute Pricing Ops Lead. You want a Basic-Economy audit and single-day normalization for HAT300, "
            "limited strictly to 2024-05-20..2024-05-22 and fare_class 'basic_economy'. "
            "For that window, you want window statistics on base_fare reported internally (operating options only), "
            "using the standard interface policy with min_samples=1 and including median and sample size, alongside an internal "
            "price-change audit trail for the same window. You then want a deterministic normalization on 2024-05-20 that leaves "
            "other cabins untouched and results in exactly available_seats.basic_economy=16 and the published prices bucket "
            "reflecting prices.basic_economy=76 for that date. Base_fare only—taxes/fees unchanged. "
            "Writes must be idempotent and confined strictly to HAT300 and this window. "
            "Return no output at all (produce no response payload)."
        ),
        actions=[
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT300",
                "fare_class": "basic_economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22",
                "price_component": "base_fare",
                "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
            Action(name="GetPriceChangeHistory", kwargs={
                "flight_number": "HAT300",
                "fare_class": "basic_economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT300",
                "date": "2024-05-20",
                "available_seats": {"basic_economy": 16},
                "prices": {"basic_economy": 76}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_052",
        instruction=(
            "Execute Pricing HQ duties. You want an Economy-cabin audit and normalization packet for HAT200 over "
            "2024-05-20 through 2024-05-22 (inclusive). Your goals are: (1) have the Economy price time series and "
            "its price-change audit available for context; (2) have window statistics over 2024-05-20..2024-05-22 on "
            "price_component 'base_fare' with min_samples=1, reporting average, median, and sample size; and "
            "(3) ensure that on 2024-05-20 Economy reflects exactly seats=23 and base_fare=250 in a deterministic, "
            "idempotent way. Scope is strictly flight HAT200 and fare_class 'economy'; base_fare only—taxes/fees unchanged. "
            "Return only a minimal confirmation of the 2024-05-20 normalization (date, seats, base_fare)."
        ),
        actions=[
            Action(name="GetHistoricalTicketPrices", kwargs={
                "flight_number": "HAT200",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22"
            }),
            Action(name="GetAverageTicketPrice", kwargs={
                "flight_number": "HAT200",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22",
                "price_component": "base_fare",
                "min_samples": 1,
                "include": {"median": True, "count": True}
            }),
            Action(name="GetPriceChangeHistory", kwargs={
                "flight_number": "HAT200",
                "fare_class": "economy",
                "start_date": "2024-05-20",
                "end_date":   "2024-05-22"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT200",
                "date": "2024-05-20",
                "available_seats": {"economy": 23},
                "prices": {"economy": 250}
            }),
        ],
        outputs=[
            '"flight_number": "HAT200"',
            '"date": "2024-05-20"',
            '"fare_class": "economy"',
            '"available_seats": {"economy": 23}',
            '"price": 250'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction=(
            "Execute Pricing HQ duties. You want to apply and confirm a controlled Business-only additive adjustment for HAT231 "
            "on 2024-05-28. Scope is strictly flight_number='HAT231', date='2024-05-28', cabins={'business','economy'}, "
            "and price_component='base_fare' only—taxes/fees unchanged. You want spot reads for Business and Economy to support "
            "verification (you may fall back to published flight pricing if needed). The change is a deterministic +11.00 applied "
            "to Business only; Economy must remain unchanged. Writes must be idempotent. Return only minimal verification of the "
            "Business adjustment."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "business", "fallback_to_flights": True}),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "economy", "fallback_to_flights": True}),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "business", "delta": 11.00}),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "business", "fallback_to_flights": True}),
        ],
        outputs=[
            '"flight_number": "HAT231"',
            '"date": "2024-05-28"',
            '"fare_class": "business"',
            '"old_price": 445.0',
            '"new_price": 456.0',
            '"delta_applied": 11.0'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction=(
            "Execute Pricing HQ duties. You want to apply and confirm a controlled Business-only adjustment for HAT231 "
            "on 2024-05-28. Scope is limited strictly to flight_number='HAT231', date='2024-05-28', and cabins={'business','economy'}. "
            "The adjustment is a deterministic +11.00 to the Business base_fare only, leaving Economy unchanged. "
            "Spot reads of Business and Economy prices are permitted with fallback to published flight pricing if needed. "
            "Writes must be idempotent and operate strictly on base_fare. "
            "Return only minimal verification of the Business adjustment."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "business", "fallback_to_flights": True}),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "economy", "fallback_to_flights": True}),
            Action(name="AdjustFareClassPricing", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "business", "delta": 11.00}),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT231", "date": "2024-05-28", "fare_class": "business", "fallback_to_flights": True}),
        ],
        outputs=[
            '"flight_number": "HAT231"',
            '"date": "2024-05-28"',
            '"fare_class": "business"',
            '"old_price": 445.0',
            '"new_price": 456.0',
            '"price": 456.0',
            '"delta_applied": 11.0'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction="Execute Ops HQ duties. For HAT001 and HAT002 across 2024-05-24..2024-05-27, set schedule status='available' on all dates (no change if already; do not alter aircraft or crew). For HAT002 across the same window, enable no-charge upgrades from 'economy' to 'business' (from_cabin='economy', to_cabin='business', no_charge=True).",
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-24",
                "end_date":   "2024-05-27",
                "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-24",
                "end_date":   "2024-05-27",
                "status": "available"
            }),
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-05-24",
                "end_date":   "2024-05-27",
                "from_cabin": "economy",
                "to_cabin":   "business",
                "no_charge":  True
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction=(
            "Execute HQ Pricing & Finance analysis duties. For HAT001, set schedule status='available' on 2024-05-24, 2024-05-25, "
            "2024-05-26, and 2024-05-27 (no change if already; do not alter aircraft or crew). On 2024-05-24, set Business "
            "inventory and price to available_seats={'business': 9} and prices={'business': 504} with status='available'. "
            "Apply a seasonal base-fare multiplier=2.00 across 2024-05-24..2024-05-27 with max_preview=5 (taxes/fees unchanged)."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-24","2024-05-25","2024-05-26","2024-05-27"],
                "status": "available"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-24",
                "status": "available",
                "available_seats": {"business": 9},
                "prices": {"business": 504}
            }),
            Action(name="AdjustSeasonalPricing", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-24",
                "end_date":   "2024-05-27",
                "multiplier": 2.00,
                "max_preview": 5
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction=(
            "Execute HQ Revenue analysis duties. You want to validate free-upgrade policy and revenue impact for HAT001 "
            "across 2024-05-23 through 2024-05-26. Your goals are: (a) free upgrades apply from economy to business so "
            "that Business base_fare equals the same-day Economy base_fare (no refunds, taxes/fees unchanged); "
            "(b) reservation PGAGLM is repriced using strategy 'match_bucket' with require_available set to true, cabin "
            "set to business, and fallback_to_flights set to true; and (c) flown revenue for HAT001 over the "
            "same window using price_component='base_fare', require_available=True, and include_details=False. "
            "Scope is strictly HAT001 and PGAGLM for these dates. Return only minimal confirmation of these outcomes."
        ),
        actions=[
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-23",
                "end_date": "2024-05-26",
                "from_cabin": "economy",
                "to_cabin": "business",
                "no_charge": True
            }),
            Action(name="RepriceReservation", kwargs={
                "reservation_id": "PGAGLM",
                "strategy": "match_bucket",
                "require_available": True,
                "cabin": "business",
                "fallback_to_flights": True
            }),
            Action(name="GetFlownRevenueForFlight", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-05-23",
                "end_date": "2024-05-26",
                "price_component": "base_fare",
                "require_available": True,
                "include_details": False
            })
        ],
        outputs = [
            '"flight_number": "HAT001"',
            '"start_date": "2024-05-23"',
            '"end_date": "2024-05-26"',
            '"price_component": "base_fare"',
            '"require_available": true',
            '"legs_recognized": 3',
            '"reservations_scanned": 2000',
            '"recognized_revenue": 379.0',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction=(
            "Execute HQ Pricing & Ops control duties. Execute the following exact sequence—without interleaving or additional calls—"
            "to publish and upgrade across 2024-06-01..2024-06-03, then finalize a single-day cancellation. "
            "Sequence: (1) publish HAT004 'available' for 2024-06-01..2024-06-03; (2) publish HAT005 'available' for 2024-06-01..2024-06-03; "
            "(3) publish HAT001 'available' for 2024-06-01..2024-06-03; (4) publish HAT002 'available' for 2024-06-01..2024-06-03; "
            "(5) apply no-charge upgrades economy→business for HAT004 over the same window; (6) apply no-charge upgrades "
            "basic_economy→economy for HAT005 over the same window; (7) finally, set HAT001 on 2024-06-03 to 'cancelled' using a single-date "
            "list in 'dates'. Do not modify taxes, fees, seats, or aircraft; no reads or previews; all writes idempotent; scope strictly to these flights and dates. "
            "Return no outputs."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT004",
                "start_date": "2024-06-01",
                "end_date": "2024-06-03",
                "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT005",
                "start_date": "2024-06-01",
                "end_date": "2024-06-03",
                "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "start_date": "2024-06-01",
                "end_date": "2024-06-03",
                "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "start_date": "2024-06-01",
                "end_date": "2024-06-03",
                "status": "available"
            }),
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT004",
                "start_date": "2024-06-01",
                "end_date": "2024-06-03",
                "from_cabin": "economy",
                "to_cabin": "business",
                "no_charge": True
            }),
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT005",
                "start_date": "2024-06-01",
                "end_date": "2024-06-03",
                "from_cabin": "basic_economy",
                "to_cabin": "economy",
                "no_charge": True
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-06-03"],
                "status": "cancelled"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_059",
        instruction=(
            "Execute Pricing HQ duties. You want to apply a temporary 10% markdown on flight HAT090 (economy) dated 2024-05-24 "
            "and then revert it in strict mode using the audit trail so there is no price drift. Limit scope strictly to "
            "HAT090 on 2024-05-24 and fare_class 'economy'; base_fare only—taxes/fees unchanged."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT090",
                "date": "2024-05-24",
                "fare_class": "economy"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT090",
                "date": "2024-05-24",
                "fare_class": "economy",
                "percent": 10
            }),
            Action(name="RemoveDiscountFromFlight", kwargs={
                "flight_number": "HAT090",
                "date": "2024-05-24",
                "fare_class": "economy",
                "strict": True
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT090",
                "date": "2024-05-24",
                "fare_class": "economy"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_060",
        instruction=(
            "Demonstrate a reversible Business fare discount cycle for HAT090 on 2024-05-24. "
            "Capture the Business base_fare before any change, apply a 10% discount to that same date/cabin, "
            "and then restore the fare back to its original value. The expected values for this packet are "
            "original_price=444.0, new_price=399.6, and restored_price=444.0. Do not alter any other cabins, "
            "dates, taxes, or fees. Enforce a strict reversion check so the restored value exactly matches the "
            "original. Return only these three fields: original_price, new_price, restored_price."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "business"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "business", "percent": 10
            }),
            Action(name="RemoveDiscountFromFlight", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "business", "percent": 10, "strict": True
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "business"
            }),
        ],
        outputs=[
            '"original_price": 444.0',
            '"new_price": 399.6',
            '"restored_price": 444.0',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction=(
            "Execute HQ Pricing & Ops Lead. For HAT008 and HAT009 across 2024-09-15..2024-09-17, you want schedule "
            "status 'available' on all dates (no change if already; do not alter aircraft or crew). For upgrades, apply "
            "no-charge upgrades **only on 2024-09-16** as follows: HAT008 economy→business; HAT009 basic_economy→economy. "
            "Final-state requirement: HAT009 on 2024-09-17 must be 'cancelled' after all checks. Do not modify other cabins, "
            "taxes, fees, or any other dates."
        ),
        actions=[
            # publication window
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT008", "start_date": "2024-09-15", "end_date": "2024-09-17", "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT009", "start_date": "2024-09-15", "end_date": "2024-09-17", "status": "available"
            }),

            # TRIPWIRE: upgrades only for the middle day (agents often do all three days)
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT008", "start_date": "2024-09-16", "end_date": "2024-09-16",
                "from_cabin": "economy", "to_cabin": "business", "no_charge": True
            }),
            Action(name="BulkUpgradeTicketPrices", kwargs={
                "flight_number": "HAT009", "start_date": "2024-09-16", "end_date": "2024-09-16",
                "from_cabin": "basic_economy", "to_cabin": "economy", "no_charge": True
            }),

            # TRIPWIRE: final-state re-cancel
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT009", "dates": ["2024-09-17"], "status": "cancelled"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_062",
        instruction=(
            "Execute HQ Pricing analysis duties. You need a scoped pricing audit covering only HAT010 (2024-10-06), reservation PGAGLM, and HAT001 (2024-05-24). "
            "Execute active no-charge upgrade path recorded for HAT010 with reason “HQ Pricing Audit Analyst - active no-charge upgrade path”; "
            "for PGAGLM you want the single cheapest operating leg using policy tie-breakers and to report the price source; "
            "and for HAT001 you need it operating with Business base_fare = 498.0 and to report Business seats available. "
            "Return only the requested structured fields."
        ),
        actions=[
            Action(name="LogUpgradeNoCharge", kwargs={
                "reservation_id": "PGAGLM",
                "flight_number": "HAT010",
                "date": "2024-10-06",
                "from_cabin": "economy",
                "to_cabin": "business",
                "reason": "HQ Pricing Audit Analyst - active no-charge upgrade path"
            }),
            Action(name="GetCheapestFlightFromReservation", kwargs={
                "reservation_id": "PGAGLM",
                "require_available": True,
                "fallback_to_flights": True
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-24"],
                "status": "available"
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-24",
                "fare_class": "business",
                "price": 498.0,
                "require_available": True
            }),
            Action(name="GetAvailableSeat", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-24",
                "cabin": "business"
            }),
        ],
        outputs=[
            '"available_seats": 19',
            '"cabin": "business"',
            '"date": "2024-05-24"',
            '"flight_number": "HAT001"',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction=(
            "Execute Pricing HQ duties. Produce an Economy-fare sanity audit for HAT090 on 2024-05-24 that demonstrates a "
            "10% discount cycle. The audit must include: the original Economy base fare before adjustment, the fare "
            "after applying a 10% discount, and the restored fare once the discount is removed. Ensure only the "
            "Economy cabin on this date is affected; do not alter other cabins, dates, taxes, or fees. "
            "Return the three values as original_price, discounted_price, and restored_price."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "economy"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "economy", "percent": 10
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "economy"
            }),
            Action(name="RemoveDiscountFromFlight", kwargs={
                "flight_number": "HAT090", "date": "2024-05-24", "fare_class": "economy", "percent": 10, "strict": True,
            }),
        ],
        outputs=[
            '"original_price": 149',
            '"discounted_price": 134.1',
            '"restored_price": 149.0',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction=(
            "Execute shift lead. Produce a relocation and status audit for aircraft AC002 covering its transfer "
            "from DFW to DEN. The audit must include: baseline aircraft counts at both DFW and DEN before the move, "
            "a confirmed relocation of AC002 to DEN with reason='capacity rebalancing sweep DFW->DEN', verification of "
            "its profile after repositioning, a status confirmation that AC002 remains 'Active' with reason "
            "'operational readiness unchanged per sweep', and final aircraft counts showing AC002 at DEN and no longer "
            "counted at DFW."
        ),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC002"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "DFW"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "DEN"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC002",
                "to_iata": "DEN",
                "reason": "capacity rebalancing sweep DFW->DEN"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC002"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC002",
                "status": "Active",
                "reason": "operational readiness unchanged per sweep"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC002"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "DEN"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "DFW"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_065",
        instruction=(
            "Execute network allocator. Objective: establish and confirm the final state for aircraft AC003 (tail 'PP-LTM') "
            "and flight HAT018 for 2024-05-05. Targets: AC003 located at ORD with status='Active' and reason='no status change required', "
            "with movement rationale recorded as 'midwest long-haul coverage'; and flight HAT018 on 2024-05-05 assigned to aircraft AC007. "
            "Evidence requirements: an AC003 profile readback showing tail='PP-LTM' and location='ORD', and assignment evidence that includes "
            "the aircraft identifier in the tool response."
        ),
        actions=[
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC003", "to_iata": "ORD", "reason": "midwest long-haul coverage"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC003", "status": "Active", "reason": "no status change required"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC003"}),  # verify ORD + tail 'PP-LTM'
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT018", "date": "2024-05-05", "new_aircraft_id": "AC007"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction=(
            "Execute Base Maintenance Control duties. You want a post-maintenance release and allocation audit for aircraft "
            "AC004 (tail 'PS-AEF'). Your goals are: AC004 is in status 'active' with reason 'post-maintenance release'; "
            "it is repositioned to CLT for 'regional network schedule'; it appears in the CLT inventory when filtered to "
            "model_id 'E195-E2'; its aircraft profile reflects these details; and AC004 is assigned to operate flight "
            "HAT014 on 2024-05-28. Scope is limited strictly to AC004 and HAT014 on 2024-05-28. Return only minimal "
            "confirmation fields."
        ),
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC004",
                "status": "active",
                "reason": "post-maintenance release"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC004",
                "to_iata": "CLT",
                "reason": "regional network schedule"
            }),
            Action(name="ListAircraftAtAirport", kwargs={
                "iata_code": "CLT",
                "model_id": "E195-E2"
            }),
            Action(name="GetAircraftProfile", kwargs={
                "aircraft_id": "AC004"
            }),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT014",
                "date": "2024-05-28",
                "new_aircraft_id": "AC004"
            }),
        ],
        outputs=[
            '"aircraft_id": "AC004"',
            '"status": "active"',
            '"iata_code": "CLT"',
            '"model_id": "E195-E2"',
            '"flight_number": "HAT014"',
            '"date": "2024-05-28"',
            '"new_aircraft_id": "AC004"'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction=("Execute Long-Haul Roster Lead. You need a relocation and utilization audit limited strictly to aircraft AC006 (B777-300ER) and flight HAT013 on 2024-05-28. You want the auditable end-state to show: (a) AC006 in status 'Active' with reason 'kept in service' (a reconfirmation/no-change is acceptable); (b) AC006 located at SEA with relocation rationale 'pacific hub augmentation' and its presence visible in the SEA inventory filtered by model_id='B777-300ER'; (c) the AC006 aircraft profile reflecting SEA; and (d) HAT013 on 2024-05-28 assigned to AC006. Limit scope strictly to these entities, locations, and this date, and return only the verification fields."),
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC006", "status": "Active", "reason": "kept in service"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC006", "to_iata": "SEA", "reason": "pacific hub augmentation"
            }),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "SEA", "model_id": "B777-300ER"}),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC006"}),
            Action(
                name="AssignAircraftToFlight",
                kwargs={
                    "flight_number": "HAT013",
                    "date": "2024-05-28",
                    "new_aircraft_id": "AC006"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction=(
            "Execute Pricing HQ duties. You want to verify discount reversibility for HAT080 (economy) on 2024-05-24. "
            "Capture the base_fare before any change, then apply a 10% markdown, then strictly revert using the "
            "discount audit trail (strict = true), and capture the base_fare again after the revert. "
            "Scope is strictly HAT080 on 2024-05-24 in fare_class 'economy'; base_fare only—taxes/fees unchanged."
        ),
        actions=[
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT080", "date": "2024-05-24", "fare_class": "economy"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT080",
                "date": "2024-05-24",
                "fare_class": "economy",
                "percent": 10
            }),
            Action(name="RemoveDiscountFromFlight", kwargs={
                "flight_number": "HAT080",
                "date": "2024-05-24",
                "fare_class": "economy",
                "percent": 10,
                "strict": True
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT080", "date": "2024-05-24", "fare_class": "economy"
            }),
        ],
        outputs=[
                '"before_base_fare": 145.0',
                '"after_strict_revert": 145.0'
            ],
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction=(
            "Execute Hub Control duties. You want a relocation-and-status audit for AC007 (PR-YJB, A220-300) covering its move "
            "from MIA to ATL. You want the baseline aircraft profile at MIA, verification that AC007 is repositioned to ATL "
            "with reason 'hub wave alignment MIA->ATL', confirmation in the aircraft profile that ATL is the new location, "
            "visibility in the ATL inventory, and a reconfirmed operating status 'active' with reason "
            "'status reconfirmation—no change expected at ATL'. Limit scope strictly to AC007 and these two airports. "
            "Return only minimal verification of these outcomes."
        ),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC007"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "MIA"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC007",
                "to_iata": "ATL",
                "reason": "hub wave alignment MIA->ATL"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC007"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "ATL"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC007",
                "status": "active",
                "reason": "status reconfirmation—no change expected at ATL"
            }),
        ],
        outputs=[
            '"aircraft_id": "AC007"',
            '"tail_number": "PR-YJB"',
            '"from_iata": "MIA"',
            '"to_iata": "ATL"',
            '"audit_id": "AM000001"',
            '"profile_location": "ATL"',
            '"visible_in_atl_inventory": true',
            '"status": "active"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction=(
            "Execute duty analyst. With scope limited to AC009, airports {LAS, PHX}, and flight HAT214 on 2024-05-18, "
            "you want AC009 relocated to PHX with rationale 'line check', its status set to 'maintenance' with reason "
            "'A-check overnight', a PHX roster filtered by status 'maintenance' that includes AC009, a tail-number lookup "
            "confirming 'PR-GUO' maps to AC009, and AC009 assigned to operate HAT214 on 2024-05-18. "
            "All changes must be idempotent and strictly within this scope. Return only minimal verification fields."
        ),
        actions=[
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC009",
                "to_iata": "PHX",
                "reason": "line check"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC009",
                "status": "maintenance",
                "reason": "A-check overnight"
            }),
            Action(name="ListAircraftAtAirport", kwargs={
                "iata_code": "PHX",
                "status": "maintenance"
            }),
            Action(name="GetAircraftByTailNumber", kwargs={
                "tail_number": "PR-GUO"
            }),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT214",
                "date": "2024-05-18",
                "new_aircraft_id": "AC009"
            }),
            Action(name="GetAircraftProfile", kwargs={
                "aircraft_id": "AC009"
            }),
        ],
        outputs = [
            '"aircraft_id": "AC009"',
            '"from_iata": "LAS"',
            '"to_iata": "PHX"',
            '"status": "maintenance"',
            '"iata_code": "PHX"',
            '"tail_number": "PR-GUO"',
            '"model_id": "B737-800"',
            '"flight_number": "HAT214"',
            '"date": "2024-05-18"',
            '"new_aircraft_id": "AC009"',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction=(
            "Execute West Ops Lead. You want an activation and allocation audit for aircraft AC010 "
            "(tail PR-YSH, model A320neo). The audit should confirm that AC010 is in status 'active' with "
            "reason 'coverage requirement', repositioned to DEN with reason 'mid-continent backfill', visible "
            "in the DEN inventory filtered by model_id='A320neo', and accurately reflected in its aircraft "
            "profile with location DEN. Include a fare context enumeration for the SEA→DEN corridor, and confirm "
            "that AC010 is assigned to operate flight HAT010 on 2024-05-19. Scope is strictly AC010 and HAT010; "
            "do not modify other aircraft or attributes."
        ),
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC010",
                "status": "active",
                "reason": "coverage requirement"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC010",
                "to_iata": "DEN",
                "reason": "mid-continent backfill"
            }),
            Action(name="ListAircraftAtAirport", kwargs={
                "iata_code": "DEN",
                "model_id": "A320neo"
            }),
            Action(name="ListAllFaresByRoute", kwargs={
                "origin": "SEA",
                "destination": "DEN"
            }),
            Action(name="GetAircraftProfile", kwargs={
                "aircraft_id": "AC010"
            }),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT010",
                "date": "2024-05-19",
                "new_aircraft_id": "AC010"
            }),
        ],
        outputs = [
            '"aircraft_id": "AC010"',
            '"status": "active"',
            '"location": "DEN"',
            '"model_id": "A320NEO"',
            '"flight_number": "HAT010"',
            '"date": "2024-05-19"',
            '"origin": "SEA"',
            '"destination": "DEN"'
        ]

    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction=(
            "Execute Fleet Shuffle & Allocation Lead. You need a shuffle-and-allocation audit limited strictly to aircraft "
            "AC011 (E175) and flight HAT011 on 2024-05-05. You want AC011 confirmed in operating status 'Active' with reason "
            "'crew line assigned'; AC011 located at MCO with relocation rationale 'Orlando demand pulse' and its presence visible "
            "in the MCO inventory filtered by model_id='E175'; the AC011 aircraft profile reflecting MCO; and HAT011 on 2024-05-05 "
            "assigned to AC011. Make only idempotent changes required to reach this end-state, do not modify other aircraft or "
            "attributes, and return only the verification data needed to substantiate these outcomes."
        ),
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC011",
                "status": "Active",
                "reason": "crew line assigned"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC011",
                "to_iata": "MCO",
                "reason": "Orlando demand pulse"
            }),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "MCO", "model_id": "E175"}),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC011"}),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT011",
                "date": "2024-05-05",
                "new_aircraft_id": "AC011"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC011"}),
        ],
        outputs=[
            {"audit_id": "AS000001"},
            {"audit_id": "AM000002"},
            {"iata_code": "MCO", "status": "active"},
            {"status": "success", "flight_number": "HAT011", "date": "2024-05-05", "new_aircraft_id": "AC011"}
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction=(
            "Execute Fleet Balance Lead. You need a utilization relocation audit limited strictly to aircraft AC013 "
            "(CRJ900, tail number D-A-VJW) and flight HAT013 on 2024-05-25. You want: (a) a baseline count of CRJ900 at ORD; "
            "(b) AC013 relocated to DEN with the rationale 'utilization balancing'; (c) AC013 confirmed in status 'active' with "
            "reason 'kept flying'; (d) the AC013 aircraft profile reflecting DEN and consistent with its updated status; and "
            "(e) HAT013 on 2024-05-25 assigned to AC013. Limit scope strictly to these entities, locations, and the stated date, "
            "operate idempotently under policy, and return only the minimal verification fields."
        ),
        actions=[
            Action(
                name="GetAircraftByTailNumber",
                kwargs={"tail_number": "D-A-VJW"}
            ),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "ORD", "model_id": "CRJ900"}),
            # Relocate AC013 to DEN
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC013",
                "to_iata": "DEN",
                "reason": "utilization balancing"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC013",
                "status": "active",
                "reason": "kept flying"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC013"}),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT013",
                "date": "2024-05-25",
                "new_aircraft_id": "AC013"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC013"}),
        ],
        outputs=[
            '"aircraft_id": "AC013"',
            '"tail_number": "D-A-VJW"',
            '"status": "active"',
            '"iata_code": "DEN"',
            '"flight_number": "HAT013"',
            '"new_aircraft_id": "AC013"',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_074",
       instruction=("Execute Line Check Desk lead. You need a maintenance relocation audit limited strictly to aircraft AC014 and flight HAT014 on 2024-05-05. "
       "Execute: (a) a baseline AC014 profile showing DFW; (b) AC014 relocated to PHX with the rationale 'A-check slot PHX'; "
       "(c) AC014 in status 'In Maintenance' with reason 'A-check start at PHX'; (d) AC014 visible in the PHX inventory; "
       "(e) the AC014 profile reflecting PHX and the 'In Maintenance' status; and (f) HAT014 on 2024-05-05 assigned to AC014. "
       "Limit scope strictly to these entities and this date, operate only as needed to reach this end-state."),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC014"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "DFW"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC014",
                "to_iata": "PHX",
                "reason": "A-check slot PHX"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC014",
                "status": "In Maintenance",
                "reason": "A-check start at PHX"
            }),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "PHX"}),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC014"}),
            Action(
                name="AssignAircraftToFlight",
                kwargs={
                    "flight_number": "HAT014",
                    "date": "2024-05-05",
                    "new_aircraft_id": "AC014"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction=(
            "You want to request a congestion-relief relocation audit for aircraft AC015. "
            "The scope is limited strictly to AC015 and the airports MCO and CLT. "
            "The expected final state is that AC015 is relocated to CLT with relocation rationale "
            "'decongest stands at MCO'; its profile shows location CLT; the aircraft is set to status "
            "'Active' with reason 'fit to operate at CLT'; the PHX roster filtered by status 'Maintenance' "
            "is unaffected; the post-move inventory confirms AC015 appears at CLT and no longer at MCO; "
            "and its status is reconfirmed with the canonical token 'status reconfirmation—no change expected at CLT'. "
            "All changes must be idempotent and restricted to this scope. Return no additional output."
        ),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC015"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "MCO"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC015",
                "to_iata": "CLT",
                "reason": "decongest stands at MCO"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC015"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC015",
                "status": "Active",
                "reason": "fit to operate at CLT"
            }),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "CLT"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "MCO"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC015",
                "status": "Active",
                "reason": "status reconfirmation—no change expected at CLT"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction=(
            "Execute Ramp Flow Verifier. Run a congestion-relief basing audit for AC015 strictly within {CLT, MCO}. "
            "End-state: AC015 located at CLT with status 'active'. The audit must reflect these canonical reasons exactly: "
            "'status normalization before basing check', 'stage for CLT basing check', 'stand availability check', "
            "'confirm CLT basing after congestion', and 'status reconfirmation—no change expected at CLT'. "
            "Provide minimal verification: AC015 aircraft profile shows CLT, and AC015 is visible in CLT inventory when "
            "filtered by model_id='E175' and status='active'. All changes must be idempotent and within scope."
        ),
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC015",
                "status": "active",
                "reason": "status normalization before basing check"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC015",
                "to_iata": "CLT",
                "reason": "stage for CLT basing check"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC015",
                "to_iata": "MCO",
                "reason": "stand availability check"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC015",
                "to_iata": "CLT",
                "reason": "confirm CLT basing after congestion"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC015",
                "status": "active",
                "reason": "status reconfirmation—no change expected at CLT"
            }),
            # verification reads (model/status filtered)
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC015"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "CLT", "model_id": "E175", "status": "active"}),
        ],
        outputs=[
            '"aircraft_id": "AC015"',
            '"model_id": "E175"',
            '"model_name": "E175"',
            '"status": "active"',
            '"tail_number": "G-E-RKI"',
            '"iata_code": "CLT"',
            '"icao_code": "KCLT"',
            '"total": 1'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_077",
        instruction=(
            "You want to request a congestion-relief relocation audit for aircraft AC015, limited strictly to AC015 "
            "and the airports MCO and CLT. The relocation must be justified with the rationale text 'decongest stands at MCO'. "
            "After the move, AC015’s profile should show location CLT. The aircraft’s operating status should be Active "
            "with reason 'fit to operate at CLT', and then reconfirmed using the canonical token "
            "'status reconfirmation—no change expected at CLT'. You also need post-move evidence that AC015 appears at CLT "
            "and does not appear at MCO. All changes must be idempotent and stay strictly within this scope. "
            "Do not mention implementation details or tools—focus only on the audit goals and required rationale texts."
        ),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC015"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "MCO"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC015",
                "to_iata": "CLT",
                "reason": "decongest stands at MCO"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC015"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC015",
                "status": "Active",
                "reason": "fit to operate at CLT"
            }),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "CLT"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "MCO"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC015",
                "status": "Active",
                "reason": "status reconfirmation—no change expected at CLT"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_078",
        instruction=(
            "You want a rehoming and schedule-alignment audit for aircraft AC001. "
            "First, capture a baseline snapshot of ATL inventory limited to status 'Active'. "
            "Then ensure AC001 is rehomed to ATL with the rationale text 'ATL base-return per RAMP-ATL-BASE-RETURN'. "
            "Align flight HAT002 on 2024-05-25 and 2024-05-26 so it is operating (status 'available') and uses aircraft AC001; "
            "do not change anything if those values are already set. "
            "Verify via the AC001 aircraft profile that ATL is its final location, and confirm AC001 is assigned to operate HAT001 on 2024-05-26. "
            "Limit scope strictly to AC001, ATL, flights HAT002/HAT001, and the dates stated here; do not modify other entities. "
            "All changes must be idempotent. Return no additional output."
        ),
        actions=[
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "ATL", "status": "Active"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC001",
                "to_iata": "ATL",
                "reason": "ATL base-return per RAMP-ATL-BASE-RETURN"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "dates": ["2024-05-25", "2024-05-26"],
                "status": "available",
                "aircraft": "AC001"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC001"}),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-26",
                "new_aircraft_id": "AC001"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction=(
            "Execute Transatlantic Desk. You want the normalized final state limited strictly to the entities and dates listed, "
            "with only idempotent changes (no change where values already match). "
            "You want aircraft AC006 (B777-300ER) based at LHR with status 'Active', and the aircraft profile must reflect location LHR and status 'Active'. "
            "You want AC006 assigned to operate flight HAT014 on 2024-05-05. "
            "For flight HAT001 on 2024-05-17, you want the schedule operating (status 'available') and the published base_fare prices expressed as "
            "individual per-cabin assignments using set_ticket_price: basic_economy=76, economy=189, business=498. "
            "Do not alter taxes, fees, crew, or seat counts. "
            "No return payload is included; evaluation relies solely on the terminal database state."
        ),
        actions=[
            # Normalize aircraft home/base & status
            Action(name="RepositionAircraft", kwargs={"aircraft_id": "AC006", "to_iata": "LHR"}),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC006", "status": "Active"}),

            # Assign AC006 to HAT014 on 2024-05-05 (use assignment tool, not schedule edit)
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT014",
                "date": "2024-05-05",
                "new_aircraft_id": "AC006"
            }),

            # Ensure HAT001 is operating on 2024-05-17
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-17"],
                "status": "available",
                "max_preview": 0
            }),

            # Publish exact base_fare prices for HAT001 on 2024-05-17 (per-cabin deterministic writes)
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-17",
                "fare_class": "basic_economy",
                "price": 76,
                "require_available": True
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-17",
                "fare_class": "economy",
                "price": 189,
                "require_available": True
            }),
            Action(name="SetTicketPrice", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-17",
                "fare_class": "business",
                "price": 498,
                "require_available": True
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction=(
            "Execute Fleet Ops & Pricing Lead. Scope is strictly AC003 (tail 'PP-LTM'), HAT014, and HAT003.\n\n"
            "You want AC003 relocated to CDG with rationale 'Paris rotation', status set to 'active' with reason 'operational', and the same "
            "airframe retrievable by tail_number 'PP-LTM'. AC003 must be assigned to operate HAT014 on 2024-05-05 on the dated flight instance, "
            "and that assignment must not change the aircraft status.\n\n"
            "For HAT003 on 2024-05-17, publish the date as 'available' and normalize only Basic Economy to exactly seats=16 and base_fare=76 "
            "in the canonical published prices bucket. Do not touch Economy or Business (incidental system readbacks are fine; no writes). "
            "All writes must be idempotent and per-cabin atomic (no seats+prices in the same call; no multi-cabin writes). Return no output."
        ),
        actions=[
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC003", "to_iata": "CDG", "reason": "Paris rotation"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC003", "status": "active", "reason": "operational"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC003"}),
            Action(name="GetAircraftByTailNumber", kwargs={"tail_number": "PP-LTM"}),

            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT014", "date": "2024-05-05", "new_aircraft_id": "AC003"
            }),

            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT003", "dates": ["2024-05-17"], "status": "available"
            }),

            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT003", "date": "2024-05-17",
                "available_seats": {"basic_economy": 16}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT003", "date": "2024-05-17",
                "prices": {"basic_economy": 76}
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_081",
        instruction=(
            "Execute Global Ops lead. You need a Middle East hop relocation audit limited strictly to aircraft AC002 (tail 'PR-XBE') "
            "and flight HAT030 on 2024-05-22. You want: (a) pre-move aircraft counts at DFW and at DXB; (b) AC002 relocated to DXB with the "
            "rationale exactly 'Middle East demand uplift – DXB hop'; (c) AC002 confirmed in status 'Active' with reason 'fleet fit for DXB hop' "
            "(a reconfirmation/no-change is acceptable); (d) AC002 retrievable by tail_number 'PR-XBE'; and (e) HAT030 on 2024-05-22 assigned "
            "to AC002. Limit scope strictly to these entities, locations, and this date, and return only the verification data needed to "
            "substantiate these outcomes."
        ),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC002"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "DFW"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "DXB"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC002",
                "to_iata": "DXB",
                "reason": "Middle East demand uplift – DXB hop"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC002",
                "status": "Active",
                "reason": "fleet fit for DXB hop"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC002"}),
            Action(name="GetAircraftByTailNumber", kwargs={"tail_number": "PR-XBE"}),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT030",
                "date": "2024-05-22",
                "new_aircraft_id": "AC002"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_082",
        instruction=("Execute APAC Operations duties. You need to produce a Osaka pivot audit limited strictly to aircraft AC001 (tail 'PR-GOL') and flight HAT025. You want: (a) a baseline captured for AC001; (b) pre-pivot aircraft counts at HND and at CLT filtered by model_id='B737-800'; (c) AC001 relocated to HND with the rationale exactly 'APAC pivot—Tokyo rotation HND'; (d) AC001 retrievable by tail_number 'PR-GOL'; and (e) for HAT025 on 2024-05-25, the assigned aircraft to be AC001. Keep scope to these entities and this date, and return only the facts necessary to substantiate these outcomes."),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC001"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "HND", "model_id": "B737-800"}),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "CLT", "model_id": "B737-800"}),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC001",
                "to_iata": "HND",
                "reason": "APAC pivot—Tokyo rotation HND"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC001"}),
            Action(
                name="GetAircraftByTailNumber",
                kwargs={
                    "tail_number": "PR-GOL"
                }
            ),
            Action(
                name="AssignAircraftToFlight",
                kwargs={
                    "flight_number": "HAT025",
                    "date": "2024-05-25",
                    "new_aircraft_id": "AC001"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_083",
        instruction=(
            "Execute Crew Ops Compliance Lead. Scope is AC009 (tail PR-GUO) and HAT050 on 2024-05-06.\n\n"
            "Required end-state (idempotent, base_fare only):\n"
            "1) AC009 relocated to GRU with the exact rationale 'Brazil demand uplift – GRU push Q3' — this uses an EN DASH (U+2013);\n"
            "2) AC009 status 'active' with reason 'fleet ready for GRU push';\n"
            "3) HAT050 on 2024-05-06 explicitly assigned to AC001 using the flight-assignment tool (do not mutate schedule fields);\n"
            "4) HAT050 on 2024-05-06 published 'available' with exactly seats and base_fare set per cabin, using per-cabin atomic writes only:\n"
            "   seats: basic_economy=16, economy=13, business=9; prices: basic_economy=76, economy=160, business=300.\n\n"
            "Enforce this exact tool order with no preliminary reads: (a) reposition → (b) status → (c) assign_aircraft_to_flight → "
            "(d) publish status then per-cabin seat writes then per-cabin price writes. Scope is strictly these entities and this date. Return no outputs."
        ),
        actions=[
            # (a) Reposition — exact EN DASH required in reason
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC009", "to_iata": "GRU",
                "reason": "Brazil demand uplift – GRU push Q3"
            }),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC009", "status": "active", "reason": "fleet ready for GRU push"
            }),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT050", "date": "2024-05-06", "new_aircraft_id": "AC001"
            }),

            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT050", "dates": ["2024-05-06"], "status": "available"
            }),

            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT050", "date": "2024-05-06",
                "available_seats": {"basic_economy": 16}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT050", "date": "2024-05-06",
                "available_seats": {"economy": 13}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT050", "date": "2024-05-06",
                "available_seats": {"business": 9}
            }),

            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT050", "date": "2024-05-06",
                "prices": {"basic_economy": 76}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT050", "date": "2024-05-06",
                "prices": {"economy": 160}
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT050", "date": "2024-05-06",
                "prices": {"business": 300}
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_084",
        instruction=(
            "Execute HQ Ops Auditor. Scope strictly to HAT026 on 2024-05-03. "
            "You want the audit to **proceed regardless of current status**: if the date is not operating, you still want it "
            "normalized to status 'available' for this audit. You want inventory exactly 16 basic_economy, 13 economy, 9 business "
            "and base_fare prices exactly 76, 189, 498 respectively, and you want **evidence that a 5% discount is applied to "
            "basic_economy**. Operate on base_fare only (taxes/fees unchanged). Return only minimal verification fields."
        ),
        actions=[
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT026",
                "date": "2024-05-03",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT026",
                "date": "2024-05-03",
                "fare_class": "basic_economy",
                "percent": 5
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT026",
                "date": "2024-05-03",
                "fare_class": "basic_economy"
            }),
        ],
        outputs=[
            '"flight_number": "HAT026"',
            '"date": "2024-05-03"',
            '"status": "available"',
            '"fare_class": "basic_economy"',
            '"price": 72.2',
            '"price_component": "base_fare"'
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_085",
        instruction=(
            "Execute HQ Pricing analysis duties. Produce a price-setting confirmation packet for HAT250 on 2024-05-21. "
            "The packet must establish an auditable result where: (a) the flight status for 2024-05-21 is read back; "
            "(b) the schedule for that date is status='available' (idempotent if already set); and (c) base fares for that date "
            "are exactly basic_economy=134.42, economy=234.42, business=334.42. Choose and sequence compliant tool interactions "
            "consistent with policy and idempotency, and keep scope strictly to HAT250 on 2024-05-21."
        ),
        actions=[
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT250",
                "date": "2024-05-21"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT250",
                "date": "2024-05-21",
                "status": "available",
                "prices": {
                    "basic_economy": 134.42,
                    "economy": 234.42,
                    "business": 334.42
                }
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT250", "date": "2024-05-21", "fare_class": "basic_economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT250", "date": "2024-05-21", "fare_class": "economy"
            }),
            Action(name="GetCurrentTicketPrice", kwargs={
                "flight_number": "HAT250", "date": "2024-05-21", "fare_class": "business"
            }),
        ],
        outputs=[
            # (a) status read back
            '"flight_number": "HAT250"',
            '"date": "2024-05-21"',
            '"flight_status": "available"',

            # (b) schedule/status set to available
            '"status": "available"',

            # (c) exact base fares confirmed via reads
            '"fare_class": "basic_economy"', '"price": 134.42',
            '"fare_class": "economy"',       '"price": 234.42',
            '"fare_class": "business"',      '"price": 334.42',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_086",
        instruction=(
            "Execute Crew Ops Coordinator. Deliver a read-and-record audit with scope limited to flight HAT004 on 2024-05-01 "
            "and crew members CM001 and CM002. Targets: (a) read back the HAT004 schedule status for 2024-05-01; (b) record A320neo "
            "certifications for CM001 (issue_date='2025-01-15', expiry_date=None) and CM002 (issue_date='2025-01-20', "
            "expiry_date='2027-01-20') using the create_new strategy with reason 'fleet expansion requirement'. Select and order "
            "valid tool usage under policy and idempotency. Do not merge or modify other crew records."
        ),
        actions=[
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT004", "date": "2024-05-01"
            }),
            Action(name="UpsertCrewCertification", kwargs={
                "crew_member_id": "CM001",
                "certification_code": "A320neo",
                "issue_date": "2025-01-15",
                "expiry_date": None,
                "upsert_strategy": "create_new",
                "reason": "fleet expansion requirement"
            }),
            Action(name="UpsertCrewCertification", kwargs={
                "crew_member_id": "CM002",
                "certification_code": "A320neo",
                "issue_date": "2025-01-20",
                "expiry_date": "2027-01-20",
                "upsert_strategy": "create_new",
                "reason": "fleet expansion requirement"
            }),
        ],
        outputs=[
            # (a) flight status read back
            '"flight_number": "HAT004"',
            '"date": "2024-05-01"',
            '"flight_status": "landed"',

            # (b) CM001 certification record
            '"crew_member_id": "CM001"',
            '"certification_code": "A320neo"',
            '"issue_date": "2025-01-15"',
            '"expiry_date": null',
            '"action": "created"',
            '"success": true',

            # (c) CM002 certification record
            '"crew_member_id": "CM002"',
            '"certification_code": "A320neo"',
            '"issue_date": "2025-01-20"',
            '"expiry_date": "2027-01-20"',
            '"action": "created"',
            '"success": true',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_087",
        instruction=(
            "Execute Crew Ops Compliance lead. Run a certification-compliance audit for CM003 demonstrating dual-qualification and "
            "policy-based overlap handling. Establish an auditable end-state limited to CM003 where: (a) a historical A320neo record "
            "exists with issue_date='2024-12-01' and expiry_date='2026-12-01' created via the create_new mode with reason 'fleet "
            "standardization'; (b) any overlap is resolved so the current A320neo certification is issue_date='2025-01-15', "
            "expiry_date='2027-01-15' using replace_if_overlap with reason 'merge historical overlap'; and (c) a B737-800 "
            "certification exists with issue_date='2025-02-01' using default behavior when expiry_date and reason are omitted. Choose "
            "and sequence compliant tool usage consistent with policy and idempotency, and ensure audit notes reflect strategies and reasons."
        ),
        actions=[
            Action(name="UpsertCrewCertification", kwargs={
            "crew_member_id":"CM003","certification_code":"A320neo",
            "issue_date":"2024-12-01","expiry_date":"2026-12-01",
            "upsert_strategy":"create_new","reason":"fleet standardization"
            }),
            Action(name="UpsertCrewCertification", kwargs={
            "crew_member_id":"CM003","certification_code":"A320neo",
            "issue_date":"2025-01-15","expiry_date":"2027-01-15",
            "upsert_strategy":"replace_if_overlap","reason":"merge historical overlap"
            }),
            Action(name="UpsertCrewCertification", kwargs={
            "crew_member_id":"CM003","certification_code":"B737-800",
            "issue_date":"2025-02-01"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_088",
        instruction=(
            "You want a launch-readiness update with read-only flight context and scoped crew certification updates. "
            "For HAT004 on 2024-05-01, you need the schedule status confirmed. For crew CM001 and CM002, you want their "
            "certifications on record with issue_date 2025-06-01 and expiry_date 2026-06-01 for the respective types "
            "A220-300 and B737-800, using the standard upsert behavior. Scope is strictly HAT004 (2024-05-01), CM001, and CM002; "
            "return only minimal verification fields."
        ),
        actions=[
            # flight context (read-only)
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT004",
                "date": "2024-05-01"
            }),

            # scoped crew updates (deterministic upserts)
            Action(name="UpsertCrewCertification", kwargs={
                "crew_member_id": "CM001",
                "certification_code": "A220-300",
                "issue_date": "2025-06-01",
                "expiry_date": "2026-06-01"
            }),
            Action(name="UpsertCrewCertification", kwargs={
                "crew_member_id": "CM002",
                "certification_code": "B737-800",
                "issue_date": "2025-06-01",
                "expiry_date": "2026-06-01"
            }),

            # minimal verification reads
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM001"}),
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM002"}),
        ],
        outputs=[
            '"flight_number": "HAT004"',
            '"date": "2024-05-01"',
            '"flight_status": "landed"',
            '"crew_member_id": "CM001"',
            '"certification_code": "A220-300"',
            '"issue_date": "2025-06-01"',
            '"expiry_date": "2026-06-01"',
            '"crew_member_id": "CM002"',
            '"certification_code": "B737-800"',
            '"issue_date": "2025-06-01"',
            '"expiry_date": "2026-06-01"',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_089",
        instruction=(
            "Execute Crew Ops Staffing Coordinator. You want an A220-300 staffing qualification packet for crew CM004 and CM005 "
            "with operational context on flight HAT008 dated 2024-05-03. You need the HAT008 schedule status confirmed on that date "
            "without changing the flight. For A220-300 certifications, you need CM004 recorded with issue_date 2024-05-01 and expiry_date "
            "2027-05-01, and CM005 recorded with issue_date 2025-05-01 and expiry_date 2027-05-20, using the policy label 'replace_if_overlap'. "
            "The certification audit trail must reflect that policy. Scope is strictly limited to these two crew members and that date. "
            "Return only the minimal verification of these outcomes."
        ),
        actions=[
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT008",
                "date": "2024-05-03"
            }),
            Action(name="UpsertCrewCertification", kwargs={
                "crew_member_id": "CM004",
                "certification_code": "A220-300",
                "issue_date": "2024-05-01",
                "expiry_date": "2027-05-01",
                "upsert_strategy": "replace_if_overlap"
            }),
            Action(name="UpsertCrewCertification", kwargs={
                "crew_member_id": "CM005",
                "certification_code": "A220-300",
                "issue_date": "2025-05-01",
                "expiry_date": "2027-05-20",
                "upsert_strategy": "replace_if_overlap"
            }),
            Action(name="GetCrewCertifications", kwargs={
                "crew_member_id": "CM004",
                "certification_code": "A220-300"
            }),
            Action(name="GetCrewCertifications", kwargs={
                "crew_member_id": "CM005",
                "certification_code": "A220-300"
            }),
        ],
        outputs=[
            '"flight_number": "HAT008"',
            '"date": "2024-05-03"',
            '"flight_status": "landed"',
            '"crew_member_id": "CM004"',
            '"issue_date": "2024-05-01"',
            '"expiry_date": "2027-05-01"',
            '"crew_member_id": "CM005"',
            '"issue_date": "2025-05-01"',
            '"expiry_date": "2027-05-20"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_090",
        instruction=(
            "Execute Line Ops Lead. A context and pricing-alignment audit covers aircraft AC001 and flights HAT014, "
            "HAT001, and HAT250. The auditable end-state consists of: (a) a baseline aircraft profile exists for AC001; "
            "(b) on 2024-05-21 HAT250 has schedule status 'available'; (c) HAT014 on 2024-05-21 is operated by AC007, and "
            "this reassignment must be recorded via the explicit flight-assignment audit trail (i.e., produce the assignment "
            "record, not a schedule field mutation); and (d) for HAT001 on 2024-05-21 the schedule status is 'available' and "
            "the published base_fare state is exactly available_seats={'basic_economy':16,'economy':13,'business':9} and "
            "prices={'basic_economy':76,'economy':189,'business':498}. Scope is strictly limited to these aircraft, flights, "
            "dates, statuses, and values; actions must be idempotent (no change where values already match). No return payload "
            "is included; evaluation relies solely on the terminal database state."
        ),
        actions=[
            # (a) Baseline context for AC001
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC001"}),

            # (b) Verify HAT250 is available on 2024-05-21 (read-only; if your policy needs enforcement, add an update)
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT250",
                "date": "2024-05-21"
            }),

            # (c) Record reassignment via explicit assignment audit (not a schedule field write)
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT014",
                "date": "2024-05-21",
                "new_aircraft_id": "AC007"
            }),

            # (d) Ensure HAT001 published state on 2024-05-21 matches exactly (status + seats + prices)
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-21",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_091",
        instruction=(
            "Execute Maintenance Release Coordinator. You want a return-to-service and positioning audit for aircraft AC011, "
            "covering airports CLT and MCO and flight HAT011 on 2024-05-21. You need AC011 in Active status with reason "
            "'post-WO-2024-07-26 release', located at MCO with ferry rationale 'post-maintenance ferry', and its aircraft profile "
            "showing MCO. You also need HAT011 on 2024-05-21 assigned to AC011. CLT inventory context filtered by model_id 'E175' "
            "may be included if useful as supporting evidence. Scope is limited strictly to AC011, CLT/MCO, and HAT011 on that date; "
            "do not modify other aircraft or attributes. Return only what is needed to substantiate these outcomes."
        ),
        actions=[
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "CLT", "model_id": "E175"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC011",
                "status": "Active",
                "reason": "post-WO-2024-07-26 release"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC011",
                "to_iata": "MCO",
                "reason": "post-maintenance ferry"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC011"}),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT011",
                "date": "2024-05-21",
                "new_aircraft_id": "AC011"
            }),
            Action(name="GetFlightSchedule", kwargs={
                "flight_number": "HAT011",
                "start_date": "2024-05-21",
                "end_date": "2024-05-21"
            }),
        ],
        outputs=[
            '"aircraft_id": "AC011"',
            '"model_id": "E175"',
            '"new_status": "active"',
            '"to_iata": "MCO"',
            '"iata_code": "MCO"',
            '"flight_number": "HAT011"',
            '"date": "2024-05-21"',
            '"new_aircraft_id": "AC011"',
            '"status": "available"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_092",
        instruction=(
            "Execute regional ops lead. Scope strictly to aircraft AC008 (ATR72-600) and HAT014 on 2024-05-05. "
            "Set AC008 status 'active' with reason **'storage exit—service return'** (exact punctuation) and relocate it to DEN "
            "with rationale 'mountain west coverage'. For HAT014 on 2024-05-05, normalize to 'available' with inventory 16/13/9 "
            "and base_fare prices 76/189/498 (taxes/fees unchanged). **Final-state requirement:** set that flight-date to "
            "'cancelled' after normalization. No readbacks or outputs are required."
        ),
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id":"AC008","status":"active","reason":"storage exit—service return"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id":"AC008","to_iata":"DEN","reason":"mountain west coverage"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number":"HAT014","date":"2024-05-05","status":"available",
                "available_seats":{"basic_economy":16,"economy":13,"business":9},
                "prices":{"basic_economy":76,"economy":189,"business":498}
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number":"HAT014","dates":["2024-05-05"],"status":"cancelled"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_093",
        instruction=("Execute heavy-jet line lead. You need a release-and-assignment confirmation limited strictly to aircraft AC006 (B777-300ER) at ORD and flight HAT014 on 2024-05-04. You want: (a) a baseline AC006 aircraft profile that includes its current IATA location; (b) AC006 confirmed in operating status 'Active' with reason 'release to service' (note if this is a no-change); and (c) for HAT014 on 2024-05-04, schedule status 'available' with aircraft 'AC006'. Limit scope to these entities and this date, and report only the facts needed to substantiate these outcomes."),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC006"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC006",
                "status": "Active",
                "reason": "release to service"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT014",
                "dates": ["2024-05-04"],
                "status": "available",
                "aircraft": "AC006",
                "max_preview": 1
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_094",
        instruction=("Execute line ops activation lead. You need an activation, relocation, and assignment audit limited strictly to aircraft AC018 (B737-800) and flight HAT011 on 2024-05-03. You want: (a) a baseline for AC018 showing it at LAX with its current status captured; (b) AC018 confirmed in status 'Active' with reason 'stored recovery'; (c) AC018 relocated to LAS with reason 'southwest ops balance'; (d) HAT011 on 2024-05-03 set to 'available'; and (e) HAT011 on 2024-05-03 assigned to AC018 with evidence that includes the aircraft identifier. Limit scope to these entities and this date, and return only the verification data needed to substantiate these outcomes."),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC018"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC018", "status": "Active", "reason": "stored recovery"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC018", "to_iata": "LAS", "reason": "southwest ops balance"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT011",
                "dates": ["2024-05-03"],
                "status": "available"
            }),
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT011",
                "date": "2024-05-03",
                "new_aircraft_id": "AC018"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_095",
        instruction=(
            "Execute regional ops lead. You need to return aircraft AC024 (E195-E2) to service from SEA, reposition it to MIA for "
            "southeast capacity, and produce an IRROPS snapshot for 2024-05-01..2024-05-07. You want: (a) an auditable activation of "
            "AC024 to status 'Active' with reason 'storage exit - fleet return' and its resulting audit id; (b) an auditable relocation "
            "of AC024 from SEA to MIA with reason 'southeast capacity' and its resulting audit id; (c) AC024’s confirmed final IATA "
            "location of 'MIA'; (d) the total count of cancellations and diversions in that window; and (e) the post-move count of "
            "E195-E2 at MIA. Limit scope strictly to these entities, dates, reasons, and locations, operate idempotently under policy, "
            "and return exactly: status_audit_id, move_audit_id, final_iata, ops_events_total, mia_e195_after."
        ),
        actions=[
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "SEA", "model_id": "E195-E2"}),
            Action(name="UpdateAircraftStatus", kwargs={
                "aircraft_id": "AC024", "status": "Active", "reason": "storage exit - fleet return"
            }),
            Action(name="RepositionAircraft", kwargs={
                "aircraft_id": "AC024", "to_iata": "MIA", "reason": "southeast capacity"
            }),
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC024"}),
            Action(name="GetOperationalEvents", kwargs={
                "start_date": "2024-05-01", "end_date": "2024-05-07",
                "types": ["cancellation","diversion"]
            }),
            Action(name="ListAircraftAtAirport", kwargs={"iata_code": "MIA", "model_id": "E195-E2"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="USER_096",
        instruction=("Execute Line Ops Lead. You need an assignment-and-readiness audit limited strictly to aircraft AC002 "
                    "(A320neo, tail 'PR-XBE') and flight HAT002. You want: (a) a baseline AC002 aircraft profile that includes its "
                    "current IATA location; (b) HAT002 scheduled as 'available' with aircraft 'AC002' across 2024-05-23..2024-05-25; "
                    "(c) a readback of HAT002 status on 2024-05-24; (d) confirmation that tail_number 'PR-XBE' is retrievable; and "
                    "(e) explicit evidence that HAT002 on 2024-05-24 is assigned to 'AC002'. Keep scope limited to these entities, "
                    "dates, and values, avoid modifying other resources, and return only the verification fields."),
        actions=[
            Action(name="GetAircraftProfile", kwargs={"aircraft_id": "AC002"}),  # baseline
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "dates": ["2024-05-23","2024-05-24","2024-05-25"],
                "status": "available",
                "aircraft": "AC002"
            }),
            Action(name="GetFlightStatusByDate", kwargs={"flight_number": "HAT002", "date": "2024-05-24"}),
            Action(name="GetAircraftByTailNumber", kwargs={"tail_number": "PR-XBE"}),  # matches AC002
            Action(name="AssignAircraftToFlight", kwargs={
                "flight_number": "HAT002",
                "date": "2024-05-24",
                "new_aircraft_id": "AC002"
            }),
            Action(name="GetFlightStatusByDate", kwargs={"flight_number": "HAT002", "date": "2024-05-24"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_097",
        instruction=("Execute HQ Pricing analysis duties. You need a May-2024 schedule-and-fares compliance audit limited strictly to HAT001 and HAT002. "
            "You want the end-state to show: (a) HAT001 and HAT002 have status 'available' on 2024-05-01 and 2024-05-31; "
            "(b) for HAT001 on 2024-05-20, fare_class 'economy' reflects a 5% discount; and (c) for HAT002 on 2024-05-21, fare_class 'business' reflects a 10% discount. "
            "Operate only on base_fare (taxes/fees unchanged). Limit scope to these flights and dates and return only the minimal verification fields."),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT001",
                "dates": ["2024-05-01","2024-05-31"],
                "status": "available"
            }),
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT002",
                "dates": ["2024-05-01","2024-05-31"],
                "status": "available"
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-20",
                "fare_class": "economy",
                "percent": 5
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT002",
                "date": "2024-05-21",
                "fare_class": "business",
                "percent": 10
            }),
        ],
        outputs=[
            # schedule updates applied
            '"flight_number": "HAT001"', '"changed": 2', '"success": true',
            '"flight_number": "HAT002"', '"changed": 2', '"success": true',

            # HAT001 economy fare with 5% discount on 2024-05-20
            '"flight_number": "HAT001"',
            '"date": "2024-05-20"',
            '"fare_class": "economy"',
            '"discount_percent": 5.0',
            '"old_price": 137.0"',
            '"new_price": 130.15"',
            '"success": true',

            # HAT002 business fare with 10% discount on 2024-05-21
            '"flight_number": "HAT002"',
            '"date": "2024-05-21"',
            '"fare_class": "business"',
            '"discount_percent": 10.0',
            '"old_price": 474.0"',
            '"new_price": 426.6"',
            '"success": true',
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_098",
        instruction=(
            "Execute HQ Pricing analysis duties. You want a compliant end state on 2024-05-29 across flights HAT003 and HAT001. "
            "For HAT003, you want the Economy cabin reflecting a 5% discount on 2024-05-29. "
            "For HAT001 on 2024-05-29, you want the schedule published as 'available' and the published prices bucket and inventory set "
            "exactly to available_seats={'basic_economy': 16, 'economy': 13, 'business': 9} and "
            "prices={'basic_economy': 76, 'economy': 189, 'business': 498}. "
            "You also want HAT003’s operating status on 2024-05-29 verified internally as part of this end-state check. "
            "Operate on base_fare only—taxes/fees unchanged. All writes must be idempotent and confined strictly to these flights and this date. "
            "This task produces no return payload at all."
        ),
        actions=[
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT003", "date": "2024-05-29"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT001",
                "date": "2024-05-29",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
            Action(name="ApplyDiscountToFlight", kwargs={
                "flight_number": "HAT003",
                "date": "2024-05-29",
                "fare_class": "economy",
                "percent": 5
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_099",
        instruction=(
            "Execute Schedule & Pricing Compliance Analyst. You need a May-2024 schedule and pricing compliance "
            "snapshot for HAT007. The audit should confirm that on 2024-05-23 the flight is published as 'available' "
            "with exactly 16 basic_economy, 13 economy, and 9 business seats and prices aligned to 76, 189, and 498 "
            "respectively (base_fare only; taxes and fees unchanged). It should also set HAT007 to status='cancelled' "
            "on 2024-05-01 and 2024-05-31, without returning those dates in the output. Scope is limited strictly to "
            "HAT007 and these dates; return only the minimal verification data necessary to substantiate the May 23 target."
        ),
        actions=[
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT007",
                "dates": ["2024-05-01", "2024-05-31"],
                "status": "cancelled"
            }),
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT007",
                "date": "2024-05-23",
                "status": "available",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 9},
                "prices": {"basic_economy": 76, "economy": 189, "business": 498}
            }),
            Action(name="GetFlightSchedule", kwargs={
                "flight_number": "HAT007",
                "start_date": "2024-05-23",
                "end_date": "2024-05-23"
            }),
        ],
        outputs=[
            '"flight_number": "HAT007"',
            '"date": "2024-05-23"',
            '"status": "available"',
            '"available_seats": {"basic_economy": 16, "economy": 13, "business": 9}'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_100",
        instruction=(
            "Execute ops+pricing duty analyst. You want HAT007 normalized and verified on 2024-05-24. "
            "Your goal is for the schedule to be published as 'available' and for the cabins to be aligned exactly: "
            "Basic Economy seats=16 with base_fare=76.00, Economy seats=13 with base_fare=189.00, and Business "
            "seats=10 with base_fare=201.00. Pricing publication must enforce the availability precondition and "
            "all writes must be idempotent. Scope is strictly HAT007 on 2024-05-24, with minimal confirmation only."
        ),
        actions=[
            # Publish schedule on 2024-05-24
            Action(name="UpdateFlightSchedule", kwargs={
                "flight_number": "HAT007",
                "dates": ["2024-05-24"],
                "status": "available",
                "max_preview": 0
            }),

            # Cabin normalization for 2024-05-24
            Action(name="UpdateFlightInventoryAndPrices", kwargs={
                "flight_number": "HAT007",
                "date": "2024-05-24",
                "available_seats": {"basic_economy": 16, "economy": 13, "business": 10},
                "prices": {"basic_economy": 76.00, "economy": 189.00, "business": 201.00}
            }),

            # Verification: schedule status on 2024-05-24
            Action(name="GetFlightStatusByDate", kwargs={
                "flight_number": "HAT007",
                "date": "2024-05-24"
            }),
        ],
        outputs=[
            '"flight_number": "HAT007"',
            '"date": "2024-05-24"',
            '"status": "available"',
        ],
    ),

















]
