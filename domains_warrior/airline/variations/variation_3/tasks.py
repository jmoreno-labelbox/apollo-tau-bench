from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="user_1",
        instruction="You are a crew manager responsible for optimizing crew info. You need to work with: crew member CM013, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320neoneo, expiry threshold days 30, start date 2024-05-16, end date 2024-05-16. Your goals are to: ensure correct crew info for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM013 and CM020 for operational assignments, put aircraft AC003 under maintenance, check crew certification status for A320neo aircraft with expiry threshold of 30 days, and review operational events within the specified window.",
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-16', "end_date": '2024-05-16'}
            ),
        ],
        outputs=[]
    ),

    
    Task(
        annotator="0",
        user_id="user_2",
        instruction="You are a senior operations manager responsible for comprehensive customer service operations and flight management. A customer has an existing reservation NO6JO3 that needs to be upgraded to FIRST class with travel insurance using payment method credit_card_4421486. You need to verify the current reservation details, access the customer profile for service history, process the upgrade according to airline policies, monitor the operational status of the customer's flight, review the daily flight schedule for operational coordination, and identify alternative flight options from JFK to ORD for potential rebooking needs. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, and provide comprehensive flight search capabilities for route planning and customer flexibility. You have access to manage: reservation lifecycle management, customer profile handling, flight status monitoring, schedule management, and flight search operations.",
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'mia.li3818@example.com'}
            ),
            Action(
                name="update_reservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="find_flights",
                kwargs={'origin': 'JFK', 'destination': 'ORD', 'date': '2024-05-16', 'cabin_class': 'business'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_3",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM016 and CM018 need activation for operational assignments with CM016 promoted to Captain role. You need to finalize their arrangements with the following details:\n"
            "- Crew members: CM016 and CM018 (activation required)"
            "- Status updates: Active status for both crew members"
            "- Role assignment: Captain for CM016 (promotion needed)"
            "- Role assignment: If there is someone not already Captain but holds B737-800 verification, promote them to Captain given they are active."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM016'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM018'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM016', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM018', "new_status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM016', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B737-800'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM006'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM006', "role": 'Captain'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_4",
        instruction=(
            "You are 'operations.manager@airline.com' responsible for comprehensive flight operations coordination and customer service management. You need to retrieve reservation details for NO6JO3, get Mia Li's profile, monitor HAT083 flight status on 2024-05-16, review flight schedules for 2024-05-16, assess operational events at ORD airport, coordinate ORD airport facilities, verify B737-800 aircraft specifications, and retrieve CM001 crew member information for optimal operational readiness.\n"
            "- Reservation ID: NO6JO3 (details verification required)"
            "- Customer email: mia.li3818@example.com (profile retrieval)"
            "- Flight monitoring: HAT083 on 2024-05-16 (status verification)"
            "- Schedule coordination: Daily operations for 2024-05-16"
            "- Operational assessment: Events at ORD on 2024-05-16"
            "- Airport coordination: ORD facilities details"
            "- Aircraft specifications: B737-800 model verification"
            "- Crew management: CM001 qualifications assessment"
            "- Notes: Comprehensive flight operations coordination including reservation management, profile retrieval, flight monitoring, schedule coordination, operational assessment, airport facilities, aircraft specifications, and crew qualifications for optimal service delivery."
        ),
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'mia.li3818@example.com'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="get_operational_events",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'ORD'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={'iata_code': 'ORD'}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={'model_id': 'B737-800'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={'crew_id': 'CM001'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_5",
        instruction="You are a senior operations manager responsible for comprehensive customer service operations and flight management. You need to work with: reservation NO6JO3, customer mia.li3818@example.com, cabin class first, insurance yes, payment method credit_card_4421486, flight HAT083, date 2024-05-16, start date 2024-05-16, end date 2024-05-16, airport ORD, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through complete reservation lifecycle management, ensure efficient flight operations and strategic scheduling, provide operational awareness through event monitoring, and handle reservation modifications including cancellations. You have access to manage: reservation lifecycle management, customer profile handling, flight status monitoring, schedule management, and operational event tracking. The objective is to get reservation details for NO6JO3, get customer profile for mia.li3818@example.com, update reservation NO6JO3 to first class with insurance and payment method credit_card_4421486, confirm the updated reservation details, get flight status for HAT083 on 2024-05-16, get flight schedule for 2024-05-16, cancel reservation NO6JO3 after upgrade completion, and get operational events at ORD airport on 2024-05-16.",
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'mia.li3818@example.com'}
            ),
            Action(
                name="update_reservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="cancel_reservation",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_operational_events",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'ORD'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_6",
        instruction="You are a crew manager responsible for optimizing crew scheduling and operational readiness. You want to activate crew members CM013 and CM020 for operational assignments, put aircraft AC003 under maintenance.",
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_7",
        instruction=(
            "You are a senior operations manager responsible for reservation management and customer service. You need to work with customer Lucas Brown and manage reservation UX0R03 for flights HAT289 and HAT135. Your responsibilities include:\n"
            "- Customer: Lucas Brown (email: lucas.brown9700@example.com)"
            "- Reservation: UX0R03 (upgrade to first class with travel insurance)"
            "- Flight route: ORD to PHL to ORD on 2024-05-22"
            "- Flight HAT289: ORD to PHL on 2024-05-22 (price: $1543)"
            "- Flight HAT135: PHL to ORD on 2024-05-22 (price: $1404)"
            "- Cabin class: First class upgrade"
            "- Insurance: Travel insurance activation"
            "- Payment method: credit_card_7872117"
            "- Notes: Comprehensive reservation management including customer profile retrieval, reservation upgrade processing, flight itinerary management, and payment processing for enhanced service delivery."
        ),        
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'UX0R03'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'lucas.brown9700@example.com'}
            ),
            Action(
                name="update_reservation",
                kwargs={'reservation_id': 'UX0R03', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_7872117', 'flights': [{'origin': 'ORD', 'destination': 'PHL', 'flight_number': 'HAT289', 'date': '2024-05-22', 'price': 1543}, {'origin': 'PHL', 'destination': 'ORD', 'flight_number': 'HAT135', 'date': '2024-05-22', 'price': 1404}]}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'UX0R03'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_8",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling. You need to finalize their arrangements with the following details:\n"
            "- Crew members: CM013 and CM020 (activation required)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Performance assessment: CM008 metrics review"
            "- Availability check: Captain role (Active status)"
            "- Aircraft: AC003 (maintenance scheduling required)"
            "- Notes: Comprehensive crew management and aircraft coordination for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_9",
        instruction="You are a senior crew operations manager responsible for comprehensive crew management, aircraft maintenance coordination, and airport facility evaluation. You need to work with: crew member CM008 (Isabella Brown) based at LAS airport, crew member CM013 (Linda Johnson) based at ORD airport, crew member CM020 (Patricia Johnson) based at CLT airport, aircraft AC003 (B787-9 Dreamliner), O'Hare International Airport (ORD), certification type A320neo, expiry threshold days 30, role Captain, status Active. Your goals are to: ensure optimal crew placement and operational readiness, maintain service quality standards through strategic crew management, coordinate aircraft maintenance scheduling, and evaluate airport facilities for crew base operations. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and airport facility assessment. The objective is to evaluate crew member CM008 performance metrics, activate crew members CM013 and CM020 for operational assignments, update CM013's role to Captain, schedule maintenance for aircraft AC003, verify A320neo certification status, and assess ORD airport capabilities for crew operations.",
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs=[]
    ),
        
    Task(
        annotator="0",
        user_id="user_10",
        instruction=(
            "You are 'operations.manager@airline.com' responsible for comprehensive reservation management and operational coordination. You need to retrieve Emma Jackson's profile, manage reservation KDBNYP with business class upgrade, find alternative flights from ORD to IAH on 2024-05-01, monitor HAT083 flight status on 2024-05-27, assess operational events, coordinate ORD airport facilities, and review AC003 maintenance logs for optimal operational readiness.\n"
            "- Customer email: emma.jackson2892@example.com (gold tier profile)"
            "- Reservation ID: KDBNYP (business class upgrade required)"
            "- Flight search: ORD to IAH on 2024-05-01 (alternative options)"
            "- Upgrade details: Business class, insurance yes, 2 total baggages"
            "- Flight monitoring: HAT083 on 2024-05-27 (status verification)"
            "- Operational assessment: May 27, 2024 events and disruptions"
            "- Airport coordination: ORD facilities details"
            "- Maintenance review: AC003 logs on 2024-05-27"
            "- Notes: Comprehensive reservation management including profile retrieval, flight search, business class upgrade, flight monitoring, operational assessment, airport coordination, and maintenance review for enhanced service delivery."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-01"}
            ),
            Action(
                name="update_reservation",
                kwargs={"reservation_id": "KDBNYP", "cabin": "business", "insurance": "yes", "total_baggages": 2, "payment_method_id": "credit_card_2599463"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={"flight_number": "HAT083", "date": "2024-05-27"}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": "AC003", "start_date": "2024-05-27", "end_date": "2024-05-27"}
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_11",
        instruction=(
            "You are 'operations.manager@airline.com'. Emma Jackson (emma.jackson2892@example.com) needs to update her reservation KDBNYP and upgrade her membership status. You need to finalize the arrangements with the following details:\n"
            "- Customer: Emma Jackson (profile verification required)"
            "- Reservation: KDBNYP (update processing needed)"
            "- Route: ORD to EWR via IAH (routing analysis)"
            "- Date: 2024-05-01 (schedule coordination)"
            "- Cabin: Business class upgrade (service enhancement)"
            "- Insurance: Coverage confirmation (protection verification)"
            "- Baggage: 2 total baggages (allowance management)"
            "- Flight: HAT083 status monitoring on 2024-05-27"
            "- Airport: ORD facilities assessment (coordination required)"
            "- Operations: Event monitoring for 2024-05-27 (disruption assessment)"
            "- Maintenance: AC003 logs review for 2024-05-27 (serviceability check)"
            "- Membership: Platinum level upgrade (loyalty enhancement)"
            "- Notes: Comprehensive reservation update with membership upgrade and operational coordination."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-01"}
            ),
            Action(
                name="update_reservation",
                kwargs={"reservation_id": "KDBNYP", "cabin": "business", "insurance": "yes", "total_baggages": 2}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={"flight_number": "HAT083", "date": "2024-05-27"}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": "AC003", "start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="update_user_membership",
                kwargs={"user_email": "emma.jackson2892@example.com", "membership_level": "platinum"}
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_12",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate both crew members for operational readiness, verify availability for Captain and Flight Attendant roles, update AC003 aircraft to Maintenance status, and check A320neo certification status within 30 days expiry threshold for optimal operational readiness.\n"
            "- Crew member CM013: activation for operational readiness"
            "- Crew member CM020: activation for operational readiness"
            "- Status management: Active status for both crew members"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo type with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including activation processing, availability verification, aircraft maintenance, and certification monitoring for optimal operational readiness."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_13",
        instruction=(
            "You are a senior operations manager responsible for comprehensive flight operations and customer service management. You need to work with customer Mia Li and manage reservation NO6JO3 for flight HAT083. Your responsibilities include:\n"
            "- Customer: Mia Li (email: mia.li3818@example.com)"
            "- Reservation: NO6JO3 (upgrade to first class with travel insurance)"
            "- Payment method: credit_card_4421486"
            "- Flight: HAT083 on 2024-05-16"
            "- Airport: ORD (Chicago O'Hare International Airport)"
            "- Schedule period: 2024-05-16 to 2024-05-16"
            "- Operational events: ORD airport monitoring for 2024-05-16"
            "- Aircraft specifications: B737-800 model details"
            "- Crew coordination: CM001 crew member information"
            "- Notes: Comprehensive operations management including reservation upgrades, customer service coordination, flight monitoring, airport assessment, schedule review, operational event monitoring, aircraft specifications analysis, and crew coordination for optimal service delivery."
        ),        
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'mia.li3818@example.com'}
            ),
            Action(
                name="update_reservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="get_operational_events",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'ORD'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={'iata_code': 'ORD'}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={'model_id': 'B737-800'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={'crew_id': 'CM001'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_14",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and A320neo certification status needs verification. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, performance assessment, role promotion, aircraft maintenance scheduling, and certification monitoring for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_15",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, role promotion, and aircraft maintenance scheduling for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_16",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and A320neo certification status needs verification. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Maintenance logs: AC003 historical records retrieval"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, role promotion, aircraft maintenance scheduling, certification monitoring, and maintenance log review for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": 'AC003'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_17",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and A320neo certification verification. Flight schedules for January 15-20, 2024 and ORD airport facilities need assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew members: CM013 and CM020 (activation required)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Performance assessment: CM008 metrics review"
            "- Availability check: Captain role (Active status)"
            "- Availability check: Flight Attendant role (Active status)"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification: A320neo verification (30-day threshold)"
            "- Flight schedules: January 15-20, 2024 period"
            "- Airport facilities: ORD details needed"
            "- Notes: Comprehensive crew management with certification verification, aircraft maintenance coordination, flight schedule planning, and airport facility assessment for operational efficiency."
        ),      
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={"start_date": '2024-01-15', "end_date": '2024-01-20'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs=[]
    ),
   
    Task(
        annotator="0",
        user_id="user_18",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance status update. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC003 maintenance status update (serviceability check)"
       ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_19",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013, CM020, and CM003 for operational assignments. Your responsibilities include:\n"
            "- Crew member CM013: Linda Johnson (Flight Attendant, LAX airport, currently Inactive)"
            "- Crew member CM020: Patricia Johnson (Flight Attendant, CLT airport, currently On Leave)"
            "- Crew member CM003: Sophia Taylor (Flight Attendant, ORD airport, currently Inactive)"
            "- Status updates: Activate both CM013 and CM020 to Active status"
            "- Role assignment: Update CM013 role to Captain"
            "- Availability monitoring: Captain role availability check (Active status)"
            "- Performance metrics: CM008 crew performance evaluation"
            "- Availability monitoring: Flight Attendant role availability check (Active status)"
            "- Aircraft management: AC003 put under maintenance"
            "- Certification monitoring: A320neo certification status with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including triple crew coordination, dual crew activation, role updates, multi-role availability verification, performance monitoring, aircraft maintenance coordination, and certification monitoring for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM003'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_20",
        instruction=(
            "You are 'baggage.manager@airline.com' responsible for comprehensive baggage management and operational coordination. You need to update baggage information for reservation 0Y69KK, verify reservation details, analyze flight-specific reservations for HAT165 on 2024-05-21, retrieve crew contact information for CM001, evaluate CM001 performance metrics, and review CM001 schedule to ensure optimal operational readiness.\n"
            "- Reservation ID: 0Y69KK (baggage update required)"
            "- Baggage management: Total 3 baggages, 1 nonfree baggage"
            "- Flight coordination: HAT165 on 2024-05-21"
            "- Reservation verification: Details confirmation needed"
            "- Flight analysis: HAT165 reservations review"
            "- Crew communication: CM001 contact information retrieval"
            "- Performance assessment: CM001 operational metrics evaluation"
            "- Schedule management: CM001 availability and assignment review"
            "- Operational readiness: Comprehensive coordination optimization"
            "- Notes: Baggage management optimization including reservation updates, flight coordination, crew communication, performance assessment, and schedule management for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="update_reservation_baggage",
                kwargs={"reservation_id": '0Y69KK', "total_baggages": 3, "nonfree_baggages": 1}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": '0Y69KK'}
            ),
            Action(
                name="get_reservations_by_flight",
                kwargs={"flight_number": 'HAT165', "date": '2024-05-21'}
            ),
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": 'CM001'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM001'}
            ),
            Action(
                name="get_crew_schedule",
                kwargs={"crew_id": 'CM001'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_21",
        instruction=(
            "You are 'operations.manager@airline.com'. Emma Jackson (emma.jackson2892@example.com) needs to cancel her reservation KDBNYP due to operational requirements. You need to finalize the cancellation with the following details:\n"
            "- Customer: Emma Jackson (profile verification required)"
            "- Reservation: KDBNYP (cancellation processing needed)"
            "- Flight: HAT165 status monitoring on 2024-05-27"
            "- Airport: ORD facilities assessment (coordination required)"
            "- Schedule: Daily operations for 2024-05-27 (planning review)"
            "- Crew: CM001 qualifications assessment (readiness verification)"
            "- Aircraft: B737-800 specifications analysis (operational planning)"
            "- Certification: B737-800 status verification (compliance check)"
            "- Operations: Event monitoring (disruption assessment)"
            "- Maintenance: AC004 logs review (serviceability check)"
            "- Notes: Comprehensive reservation cancellation with operational coordination and crew readiness assessment."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="cancel_reservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),

            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={"model_id": "B737-800"}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": "B737-800", "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": "AC004"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_22",
        instruction=(
            "You are a senior operations manager responsible for customer service operations, crew coordination, and comprehensive operational management. You need to work with customer Emma Jackson and manage reservation KDBNYP for flight HAT165. Your responsibilities include:\n"
            "- Customer: Emma Jackson (email: emma.jackson2892@example.com)"
            "- Reservation: KDBNYP (business class flight from ORD to EWR)"
            "- Goal: Customer wants to cancel the reservation"
            "- Notes: A reservation is only cancellable if booking is made less than 24 hours before request to cancel or customer is a gold tier member."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="cancel_reservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_23",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM010 and CM021 need to be activated for operational assignments with CM010 promoted to Captain role. You need to finalize their crew arrangements with the following details:\n"
            "- Crew members: CM010 and CM021 (activation required)"
            "- Role assignment: Captain for CM010 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Performance assessment: CM008 metrics review"
            "- Availability check: Captain role (Active status)"
            "- Availability check: Flight Attendant role (Active status)"
            "- Certification: B737-800 verification required"
            "- Notes: Comprehensive crew management for operational efficiency and certification compliance."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM010'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM021'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM010', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM021', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM010', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B737-800'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_24",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM016 and CM018 need activation for operational assignments with CM016 promoted to Captain role. B737-800 certification and aircraft specifications require verification. You need to finalize their arrangements with the following details:\n"
            "- Crew members: CM016 and CM018 (activation required)"
            "- Role assignment: Captain for CM016 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Performance assessment: CM008 metrics review"
            "- Availability check: Captain role (Active status)"
            "- Availability check: Flight Attendant role (Active status)"
            "- Certification: B737-800 verification required"
            "- Aircraft: B737-800 model specifications (operational details needed)"
            "- Notes: Comprehensive crew management with certification verification and aircraft coordination for operational efficiency."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM016'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM018'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM016', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM018', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM016', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B737-800'}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={"model_id": 'B737-800'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_25",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020 for operational assignments. Your responsibilities include:\n"
            "- Crew member CM013: Linda Johnson (Flight Attendant, LAX airport, currently Inactive)"
            "- Crew member CM020: Patricia Johnson (Flight Attendant, CLT airport, currently On Leave)"
            "- Status updates: Activate both CM013 and CM020 to Active status"
            "- Role assignment: Update CM013 role to Captain"
            "- Availability monitoring: Captain role availability check (Active status)"
            "- Performance metrics: CM008 crew performance evaluation"
            "- Availability monitoring: Flight Attendant role availability check (Active status)"
            "- Aircraft management: AC003 put under maintenance"
            "- Notes: Comprehensive crew management including dual crew activation, role updates, multi-role availability verification, performance monitoring, and aircraft maintenance coordination for optimal operational readiness."
        ), 
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_26",
        instruction=(
            "You are a crew manager responsible for optimizing crew info. You need to work with crew members CM013 and CM020 for operational assignments. Your responsibilities include:\n"
            "- Crew member CM013: Linda Johnson (Flight Attendant, LAX airport, currently Inactive)"
            "- Crew member CM020: Patricia Johnson (Flight Attendant, CLT airport, currently On Leave)"
            "- Status updates: Activate both CM013 and CM020 to Active status"
            "- Role assignment: Update CM013 role to Captain"
            "- Aircraft management: AC003 put under maintenance"
            "- Certification monitoring: A320neo certification status with 30-day expiry threshold"
            "- Operational monitoring: Review events for 2024-05-16"
            "- Notes: Comprehensive crew management including dual crew activation, role updates, aircraft maintenance coordination, certification monitoring, and operational event review for optimal operational efficiency."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-16', "end_date": '2024-05-16'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_27",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM010 and CM021 need activation for operational assignments with CM010 promoted to Captain role. B737-800 certification requires verification and maintenance logs need review. Performance metrics require assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM010: activation required (status update needed)"
            "- Crew member CM021: activation required (status update needed)"
            "- Role assignment: Captain for CM010 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Certification: B737-800 verification required (compliance check)"
            "- Maintenance: AC003 logs review (operational assessment)"
            "- Notes: Comprehensive crew management with role promotion, performance assessment, certification verification, and maintenance coordination for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM010'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM021'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM010', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM021', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM010', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B737-800'}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": 'AC003'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_28",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance status update and maintenance logs need review. Performance metrics require assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC003 maintenance status update (serviceability check)"
            "- Maintenance: AC003 logs review (operational assessment)"
            "- Notes: Comprehensive crew management with role promotion, performance assessment, and aircraft maintenance coordination for operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": 'AC003'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_29",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. A320neo certification requires verification and performance metrics need assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Certification: A320neo verification within 30 days expiry"
            "- Notes: Comprehensive crew management with role promotion, performance assessment, and certification verification for operational readiness."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_30",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM004 and CM008 need activation for operational assignments with CM004 promoted to Captain role and relocated to DFW. B737 certification requires verification and performance metrics need assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM004: activation required (status update needed)"
            "- Crew member CM008: activation required (status update needed)"
            "- Role assignment: Captain for CM004 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Certification: B737 verification required (compliance check)"
            "- Home base: DFW relocation for CM004 (deployment optimization)"
            "- Notes: Comprehensive crew management with role promotion, performance assessment, certification verification, and strategic base relocation for operational efficiency."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM004'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM004', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM008', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM004', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B737'}
            ),
            Action(
                name="update_crew_member_home_base",
                kwargs={"crew_id": 'CM004', "new_home_base": 'DFW'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_31",
        instruction=(
            "You are 'operations.manager@airline.com'. Chen Hernandez (chen.hernandez3740@example.com) needs to upgrade her reservation V25KYO to first class with enhanced services. You need to finalize the arrangements with the following details:\n"
            "- Customer: Chen Hernandez (profile verification required)"
            "- Reservation: V25KYO (upgrade processing needed)"
            "- Route: EWR to ORD (routing analysis)"
            "- Date: 2024-05-21 (schedule coordination)"
            "- Cabin: First class upgrade (service enhancement)"
            "- Insurance: Coverage confirmation (protection verification)"
            "- Baggage: 3 total baggages, 1 nonfree baggage (allowance management)"
            "- Payment: Credit card ending in 8453507 (payment processing)"
            "- Schedule: Daily operations for 2024-05-21 (planning review)"
            "- Operations: Event monitoring for 2024-05-21 (disruption assessment)"
            "- Airport: ORD facilities assessment (coordination required)"
            "- Crew: Flight Attendant availability check (readiness verification)"
            "- Maintenance: AC003 logs review for 2024-05-21 (serviceability check)"
            "- Notes: Comprehensive reservation upgrade with operational coordination and crew readiness assessment."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": 'chen.hernandez3740@example.com'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'V25KYO'}
            ),

            Action(
                name="get_flight_schedule",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="update_reservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'first', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": 'AC003', "start_date": '2024-05-21', "end_date": '2024-05-21'}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_32",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance status update and A320neo certification needs verification. Operational events and airport facilities require assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC003 maintenance status update (serviceability check)"
            "- Certification: A320neo verification within 30 days expiry"
            "- Operations: Event monitoring for 2024-05-27 (disruption assessment)"
            "- Airport: ORD facilities assessment (coordination required)"
            "- Notes: Comprehensive crew management with aircraft maintenance, certification verification, and operational coordination for airport readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-27', "end_date": '2024-05-27'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_33",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance status update and performance metrics need assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC003 maintenance status update (serviceability check)"
            "- Notes: Comprehensive crew management with role promotion, performance assessment, and aircraft maintenance coordination for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_34",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance status update and A320neo certification needs assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC003 maintenance status update (serviceability check)"
            "- Certification: A320neo expiry threshold 30 days (compliance check)"
            "- Operational events: May 27, 2024 monitoring (coordination review)"
            "- Notes: Comprehensive crew management with role promotion, certification monitoring, aircraft maintenance, and operational event coordination for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-27', "end_date": '2024-05-27'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_35",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC004 requires maintenance status update and A320neo certification needs assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Aircraft: AC004 maintenance status update (serviceability check)"
            "- Certification: A320neo expiry threshold 30 days (compliance check)"
            "- Notes: Comprehensive crew management with role promotion, certification monitoring, and aircraft maintenance coordination for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC004', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_36",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance status update and A320neo certification needs assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC003 maintenance status update (serviceability check)"
            "- Certification: A320neo expiry threshold 30 days (compliance check)"
            "- Operational events: May 10-12, 2024 monitoring (coordination review)"
            "- Notes: Comprehensive crew management with role promotion, certification monitoring, aircraft maintenance, and operational event coordination for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-10', "end_date": '2024-05-12'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_37",
        instruction=(
            "You are 'crew.manager@airlineops.com'. The operations team needs to optimize crew scheduling and operational readiness for the upcoming flight schedule. You need to finalize crew arrangements with the following details:\n"
            "- Crew member: CM013 (status: Active)"
            "- Crew member: CM020 (status: Active)"
            "- Role update: Update CM013's role to Captain"
            "- Availability check: Captain crew members (Active status)"
            "- Availability check: Flight Attendant crew members (Active status)"
            "- Certification verification: A320neo aircraft type"
            "- Expiry threshold: 30 days for certification monitoring"
            "- Notes: Crew activation and certification verification completed for operational readiness."
        ),      
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_38",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020 for operational assignments. Your responsibilities include:\n"
            "- Crew member CM013: Linda Johnson (Flight Attendant, LAX airport, currently Inactive)"
            "- Crew member CM020: Patricia Johnson (Flight Attendant, CLT airport, currently On Leave)"
            "- Status updates: Activate both CM013 and CM020 to Active status"
            "- Role assignment: Update CM013 role to Captain"
            "- Availability monitoring: Captain role availability check (Active status)"
            "- Availability monitoring: Flight Attendant role availability check (Active status)"
            "- Performance metrics: CM008 crew performance evaluation"
            "- Aircraft management: AC003 status scheduled for maintenance"
            "- Notes: Comprehensive crew management including dual crew activation, role updates, multi-role availability verification, performance monitoring, and aircraft maintenance coordination for optimal operational readiness."
        ),      
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
        ],
        outputs=[]   
    ),

    Task(
        annotator="0",
        user_id="user_39",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM017 need activation for operational assignments with CM013's profile updated. Aircraft AC004 requires maintenance scheduling and B737 certification status needs verification. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM017: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM017"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Profile update: CM013 profile with Active status"
            "- Aircraft maintenance: AC004 status scheduled for maintenance"
            "- Certification monitoring: B737 with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, profile updates, aircraft maintenance scheduling, and certification monitoring for optimal operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM017'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM017', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),    
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew_profile",
                kwargs={"crew_id": 'CM013', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B737', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_40",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020 for operational assignments. Your responsibilities include:\n"
            "- Crew member CM013: Linda Johnson (Flight Attendant, LAX airport, currently Inactive)"
            "- Crew member CM020: Patricia Johnson (Flight Attendant, CLT airport, currently On Leave)"
            "- Status updates: Activate both CM013 and CM020 to Active status"
            "- Role assignment: Update CM013 role to Captain"
            "- Aircraft management: AC003 put under maintenance"
            "- Availability monitoring: Flight Attendant availability check"
            "- Certification monitoring: A320neo certification status with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including status activation, role updates, aircraft maintenance coordination, and certification monitoring for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_41",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need status verification and activation for operational assignments. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: status verification (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Status update: Active status for CM020 (operational readiness)"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Notes: Crew management focusing on CM020 activation and availability verification for Captain and Flight Attendant roles to ensure operational readiness."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_42",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. A320neo certification status requires verification. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Certification: A320neo expiry threshold 30 days (compliance check)"
            "- Notes: Comprehensive crew management with role promotion, availability verification, and certification monitoring for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_43",
        instruction=(
            "You are 'operations.manager@airline.com'. Reservation V25KYO requires comprehensive update with first class upgrade, travel insurance, and enhanced baggage allowance for ORD destination on May 21, 2024. You need to finalize their arrangements with the following details:\n"
            "- Reservation: V25KYO (comprehensive update required)"
            "- Cabin: First class upgrade (premium service)"
            "- Insurance: Travel insurance coverage (comprehensive protection)"
            "- Baggage: 3 total bags, 1 non-free bag (enhanced allowance)"
            "- Payment: Credit card ending 8453507 (transaction processing)"
            "- Operational events: May 21, 2024 monitoring (disruption tracking)"
            "- Airport: ORD facilities verification (operational coordination)"
            "- Crew availability: Flight Attendant role (staffing verification)"
            "- Aircraft: B737-800 model specifications (operational planning)"
            "- Notes: Comprehensive reservation management with operational coordination, airport facilities verification, crew availability monitoring, and aircraft model analysis for service excellence."
        ),        
        actions=[
            Action(
                name="update_reservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'first', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={"model_id": 'B737-800'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_44",
        instruction=(
            "You are 'operations.manager@airline.com'. Gold customer mei.hernandez3561@example.com with reservation R9QDGB (LAX to BOS on 2024-05-28, flight HAT034) requires first class upgrade with enhanced baggage allowance. You need to finalize their arrangements with the following details:\n"
            "- Customer: Gold tier member Mei Hernandez (profile verification)"
            "- Reservation: R9QDGB (current economy class)"
            "- Flight: HAT034 on May 28, 2024 (LAX to BOS)"
            "- Upgrade: First class cabin (gold tier benefit)"
            "- Insurance: Travel insurance coverage (comprehensive protection)"
            "- Baggage: 5 total bags, 2 non-free bags (enhanced allowance)"
            "- Payment: Credit card ending 6082923 (transaction processing)"
            "- Route verification: LAX to BOS availability (operational confirmation)"
            "- Flight status: HAT034 operational readiness (service verification)"
            "- Notes: Gold tier reservation upgrade with first class cabin, travel insurance, and enhanced baggage allowance processed according to membership benefits."
        ),       
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": 'mei.hernandez3561@example.com'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": 'LAX', "destination": 'BOS', "date": '2024-05-28'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={"flight_number": 'HAT034', "date": '2024-05-28'}
            ),
            Action(
                name="update_reservation",
                kwargs={"reservation_id": 'R9QDGB', "cabin": 'first', "insurance": 'yes', "total_baggages": 5, "nonfree_baggages": 2, "payment_method_id": 'credit_card_6082923'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
        ],
        outputs=["Gold tier member profile for Mei Hernandez with account information and membership benefits", "Current reservation R9QDGB showing economy class flight from LAX to BOS on 2024-05-28", "Available flights from LAX to BOS on 2024-05-28 confirming route viability", "Flight HAT034 status for May 28, 2024 showing operational readiness", "Reservation R9QDGB successfully updated to first class with insurance and 5 total bags", "Final reservation details showing upgraded cabin class, insurance, and enhanced baggage allowance"]
    ),
    
    Task(
        annotator="0",
        user_id="user_45",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance status update. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for both crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC003 maintenance status update (serviceability check)"
            "- Notes: Comprehensive crew management with role promotion, availability verification, and aircraft maintenance coordination for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_46",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need status verification and activation for operational assignments. Aircraft AC004 requires maintenance status update and B787-9 certification needs assessment. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: status verification (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Status update: Active status for CM020 (operational readiness)"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Aircraft: AC004 status scheduled for maintenance (serviceability check)"
            "- Certification: B787-9 expiry threshold 30 days (compliance check)"
            "- Notes: Crew management focusing on CM020 activation, availability verification, aircraft maintenance, and certification compliance for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_47",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013, CM020, and CM023 need activation for operational assignments with CM013 promoted to Captain role. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: activation required (current status: Inactive)"
            "- Crew member CM020: activation required (current status: On Leave)"
            "- Crew member CM023: activation required (operational readiness)"
            "- Role assignment: Captain for CM013 (promotion needed)"
            "- Status updates: Active status for all three crew members"
            "- Availability check: Captain role (Active status verification)"
            "- Performance metrics: CM008 assessment (evaluation required)"
            "- Availability check: Flight Attendant role (Active status verification)"
            "- Notes: Comprehensive crew management with role promotion and availability verification for operational readiness across multiple crew members."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM023', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_48",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate CM020 for operational readiness, assess CM008 performance metrics, verify availability for Captain and Flight Attendant roles, update AC003 aircraft to Maintenance status, check A320neo certification status within 30 days expiry, and track operational events for 2024-05-27.\n"
            "- Crew member CM013: information retrieval for assessment"
            "- Crew member CM020: activation and information retrieval"
            "- Status management: Active status for CM020"
            "- Performance assessment: CM008 metrics evaluation"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo type with 30-day expiry threshold"
            "- Operational tracking: 2024-05-27 events and disruptions"
            "- Notes: Comprehensive crew management including information retrieval, activation processing, performance assessment, availability verification, aircraft maintenance, certification monitoring, and operational event tracking for optimal operational readiness."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),  
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-27', "end_date": '2024-05-27'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_49",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate CM020 for operational readiness, assess CM008 performance metrics, verify availability for Captain and Flight Attendant roles, check B787-9 certification status within 30 days expiry, and retrieve B787-9 aircraft model specifications for operational planning.\n"
            "- Crew member CM013: information retrieval for assessment"
            "- Crew member CM020: activation and information retrieval"
            "- Status management: Active status for CM020"
            "- Performance assessment: CM008 metrics evaluation"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Certification monitoring: B787-9 type with 30-day expiry threshold"
            "- Aircraft specifications: B787-9 model capabilities review"
            "- Operational planning: Strategic deployment optimization"
            "- Notes: Comprehensive crew management including information retrieval, activation processing, performance assessment, availability verification, certification monitoring, and aircraft model analysis for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={"model_id": 'B787-9'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_50",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate CM020 for operational readiness, verify availability for Flight Attendant roles, update AC003 aircraft to Maintenance status, and check A320neo certification status within 30 days expiry threshold for operational compliance.\n"
            "- Crew member CM013: information retrieval for assessment"
            "- Crew member CM020: activation and information retrieval"
            "- Status management: Active status for CM020"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo type with 30-day expiry threshold"
            "- Operational compliance: Certification status verification"
            "- Notes: Comprehensive crew management including information retrieval, activation processing, availability verification, aircraft maintenance, and certification monitoring for optimal operational readiness and compliance."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_51",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate CM020 for operational readiness, verify availability for Flight Attendant roles, update AC003 aircraft to Maintenance status, check A320neo certification status within 30 days expiry threshold, evaluate CM020 performance metrics, review CM020 schedule, and retrieve CM020 contact information for operational assessment.\n"
            "- Crew member CM013: information retrieval for assessment"
            "- Crew member CM020: activation and information retrieval"
            "- Status management: Active status for CM020"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo type with 30-day expiry threshold"
            "- Operational compliance: Certification status verification"
            "- Performance assessment: CM020 operational metrics evaluation"
            "- Schedule management: CM020 availability and assignment review"
            "- Contact coordination: CM020 communication information retrieval"
            "- Notes: Comprehensive crew management including information retrieval, activation processing, availability verification, aircraft maintenance, certification monitoring, performance assessment, schedule management, and contact coordination for optimal operational readiness and compliance."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="get_crew_schedule",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": 'CM020'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_52",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, verify availability for Captain and Flight Attendant roles, update AC003 aircraft to Maintenance status, monitor A320 certification status with 30-day expiry threshold, analyze A-Check maintenance logs for 2024-03-25 to 2024-03-31, and evaluate CM013 performance metrics for operational assessment.\n"
            "- Crew member CM013: information retrieval for assessment"
            "- Crew member CM020: information retrieval for assessment"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320 with 30-day expiry threshold"
            "- Maintenance analysis: A-Check logs for 2024-03-25 to 2024-03-31"
            "- Performance assessment: CM013 operational metrics evaluation"
            "- Notes: Comprehensive crew management including information retrieval, multi-role availability verification, aircraft maintenance, certification monitoring, maintenance log analysis, and performance assessment for optimal operational readiness."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"start_date": '2024-03-25', "end_date": '2024-03-31', "maintenance_type": 'A-Check'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),
        ],
        outputs=[]
        
    ),
    
        Task(
        annotator="0",
        user_id="user_53",
        instruction="You are a crew manager responsible for optimizing crew info. You need to work with: crew member CM013, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320neoneo, expiry threshold days 30, start date 2024-05-16, end date 2024-05-16. Your goals are to: ensure correct crew info for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM013 and CM020 for operational assignments, schedule aircraft AC003 status to Maintenance, check crew certification status for A320neo aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_54",
        instruction="You are a senior operations manager responsible for comprehensive customer service operations and flight management. A customer has an existing reservation NO6JO3 that needs to be upgraded to FIRST class with travel insurance using payment method credit_card_4421486. You need to verify the current reservation details, access the customer profile for service history, process the upgrade according to airline policies, monitor the operational status of the customer's flight, review the daily flight schedule for operational coordination, and identify alternative flight options from JFK to ORD for potential rebooking needs. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, and provide comprehensive flight search capabilities for route planning and customer flexibility. You have access to manage: reservation lifecycle management, customer profile handling, flight status monitoring, schedule management, and flight search operations.",
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'mia.li3818@example.com'}
            ),
            Action(
                name="update_reservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_55",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate both crew members for operational readiness, verify availability for Captain and Flight Attendant roles, update AC004 aircraft to Maintenance status, and monitor B787 certification status with 30-day expiry threshold.\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC004 status scheduled for maintenance"
            "- Certification monitoring: B787 with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including information retrieval, dual crew activation, multi-role availability verification, aircraft maintenance, and certification monitoring for optimal operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_56",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need management with CM020 activated from On Leave to Active. Aircraft AC004 requires maintenance scheduling, B787-9 certification status needs verification, and A350-900 aircraft specifications require retrieval. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval for existing Captain status"
            "- Crew member CM020: information retrieval and activation from On Leave"
            "- Status management: CM020 update to Active status"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Availability verification: First Officer role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Availability verification: Lead Flight Attendant role (Active status)"
            "- Aircraft maintenance: AC004 status scheduled for maintenance"
            "- Certification monitoring: B787-9 with 30-day expiry threshold"
            "- Aircraft specifications: A350-900 model details retrieval"
            "- Notes: Comprehensive crew management including dual crew information retrieval, status activation, multi-role availability verification across all crew categories, performance assessment, aircraft maintenance scheduling, certification monitoring, and aircraft model specifications for optimal operational coordination."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'First Officer', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Lead Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={"model_id": 'A350-900'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_57",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate both crew members for operational readiness, verify availability for Captain and Flight Attendant roles, update AC004 aircraft to Maintenance status, monitor B787 certification status with 30-day expiry threshold, and evaluate CM013 performance metrics for operational assessment.\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Performance assessment: CM013 operational metrics review"
            "- Aircraft maintenance: AC004 put under maintenance"
            "- Certification monitoring: B787 with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including information retrieval, dual crew activation, multi-role availability verification, performance assessment, aircraft maintenance, and certification monitoring for optimal operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC004', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_58",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational readiness. You need to manage crew members CM004 and CM008 for optimal deployment including role assignments, availability assessment, performance evaluation, training verification, and operational coordination.\n"
            "- Crew member CM004: information retrieval, training records verification, role management, home base update to DFW, and schedule review\n"
            "- Crew member CM008: information retrieval and performance metrics assessment\n"
            "- Availability assessment: Captain, Flight Attendant, First Officer, and Purser categories\n"
            "- Training verification: CM004 certification compliance and training status\n"
            "- Performance evaluation: CM008 operational efficiency and metrics analysis\n"
            "- Operational coordination: CM004 home base optimization and deployment readiness\n"
            "- Schedule management: CM004 assignment verification and operational effectiveness\n"
            "- Notes: Comprehensive crew management including information retrieval, training verification, availability assessment, performance evaluation, role management, home base optimization, and schedule coordination for operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM004'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="get_crew_training_records",
                kwargs={"crew_id": 'CM004'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'First Officer', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Purser', "status": 'Active'}
            ),
            Action(
                name="update_crew_member_home_base",
                kwargs={"crew_id": 'CM004', "new_home_base": 'DFW'}
            ),
            Action(
                name="get_crew_member_schedule",
                kwargs={"crew_id": 'CM004'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_59",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM004 and CM008 need activation for operational assignments with CM004's home base updated to DFW. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM004: information retrieval and home base update"
            "- Crew member CM008: information retrieval and performance assessment"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Availability verification: First Officer role (Active status)"
            "- Availability verification: Purser role (Active status)"
            "- Home base update: CM004 to DFW for optimal deployment"
            "- Schedule review: CM004 operational assignments verification"
            "- Notes: Comprehensive crew management including dual crew information retrieval, multi-role availability verification across all crew categories, performance assessment, strategic home base optimization, and operational schedule review for enhanced deployment efficiency."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM004'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'First Officer', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Purser', "status": 'Active'}
            ),
            Action(
                name="update_crew_member_home_base",
                kwargs={"crew_id": 'CM004', "new_home_base": 'DFW'}
            ),
            Action(
                name="get_crew_member_schedule",
                kwargs={"crew_id": 'CM004'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_60",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve contact information for CM001, assess CM002 performance metrics, review CM001 schedule, verify CM002 training records, get CM001 member information, check CM002 certification status, and retrieve B737-800 model specifications for strategic planning.\n"
            "- Crew member CM001: contact info retrieval and schedule review"
            "- Crew member CM002: performance assessment and training verification"
            "- Performance metrics: CM002 operational efficiency analysis"
            "- Schedule coordination: CM001 assignments and duty periods"
            "- Training records: CM002 certification compliance verification"
            "- Certification status: CM002 aviation regulations compliance"
            "- Aircraft specifications: B737-800 model capabilities review"
            "- Notes: Comprehensive crew management including contact information retrieval, performance assessment, schedule coordination, training verification, certification compliance, and aircraft model analysis for optimal operational readiness."
        ),       
        actions=[
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": "CM002"}
            ),
            Action(
                name="get_crew_schedule",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="get_crew_training_records",
                kwargs={"crew_id": "CM002"}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"crew_id": "CM002"}
            ),
            Action(
                name="get_aircraft_model_info",
                kwargs={"model_id": "B737-800"}
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_61",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020, and aircraft AC003. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Performance evaluation: CM008 metrics assessment"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Aircraft status: AC003 put under maintenance"
            "- Certification check: A320neo with 30-day expiry threshold"
            "- Notes: Crew members activated, role assigned, performance evaluated, availability verified, aircraft status updated, and certification checked for operational readiness."
        ), 
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_62",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling, A320neo certification status needs verification, and performance metrics require evaluation. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Performance evaluation: CM020 operational metrics retrieval"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, performance assessment for both CM008 and CM020, role promotion, aircraft maintenance scheduling, and certification monitoring for optimal operational readiness and crew deployment efficiency."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": "CM020"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_63",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational readiness. You need to activate crew members CM013 and CM020, assign CM013 to Captain role, verify availability for Captain and Flight Attendant positions, assess CM008 performance metrics, and monitor A320neo certifications within 30 days expiry. Retrieve current assignments for CM013 to ensure optimal crew placement.\n"
            "- Crew member CM013: activation, Captain role assignment, and assignment retrieval"
            "- Crew member CM020: activation for operational readiness"
            "- Status management: Active status for both crew members"
            "- Role assignments: Captain for CM013"
            "- Availability verification: Active Captain and Flight Attendant roles"
            "- Performance assessment: CM008 metrics evaluation"
            "- Certification monitoring: A320neo type with 30-day expiry threshold"
            "- Assignment management: Current assignments retrieval for CM013"
            "- Notes: Comprehensive crew management including activation processing, role assignments, availability verification, performance assessment, certification monitoring, and assignment retrieval for optimal operational readiness."
        ),      
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="manage_crew_member",
                kwargs={"action": "get_assignments", "crew_id": "CM013"}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_64",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Performance evaluation: CM008 metrics assessment"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Status management: Dual crew activation for operational readiness"
            "- Role coordination: Captain leadership assignment"
            "- Notes: Crew members activated, role assigned, performance evaluated, and availability verified for comprehensive crew management."
        ),     
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),  
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_65",
        instruction=(
            "You are 'customer.service@airline.com' responsible for comprehensive account services for emma.jackson2892@example.com. You need to handle reservation KDBNYP including cancellation and alternative flight discovery from ORD to IAH on 2024-05-27. Monitor flight HAT165 status, coordinate ORD airport facilities, manage flight schedules for 2024-05-27, upgrade membership to platinum, and retrieve crew contact information for CM013.\n"
            "- Customer email: emma.jackson2892@example.com"
            "- Reservation ID: KDBNYP (requires cancellation)"
            "- Alternative flight search: ORD to IAH on 2024-05-27"
            "- Flight monitoring: HAT165 on 2024-05-27"
            "- Airport coordination: ORD facilities"
            "- Schedule management: 2024-05-27 flight operations"
            "- Membership upgrade: platinum level"
            "- Crew contact: CM013 for operational coordination"
            "- Notes: Comprehensive customer service management including profile retrieval, reservation lifecycle, flight discovery, status monitoring, airport coordination, schedule optimization, membership enhancement, and crew communication."
        ),
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="cancel_reservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),
            Action(
                name="find_flights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-27"}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="update_user_membership",
                kwargs={"user_email": "emma.jackson2892@example.com", "membership_level": "platinum"}
            ),
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": "CM013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_66",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and A320neo certification status needs verification. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, performance assessment, role promotion, aircraft maintenance scheduling, and certification monitoring for optimal operational readiness and crew deployment efficiency."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": "CM013"}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_67",
        instruction=(
            "You are a crew manager responsible for comprehensive crew management and operational coordination. You need to work with crew members CM013, CM020, and CM008. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Performance evaluation: CM008 metrics assessment"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Schedule management: CM008 operational planning"
            "- Contact coordination: CM008 communication details"
            "- Status management: Dual crew activation for operational readiness"
            "- Notes: Crew members activated, performance evaluated, availability verified, schedule retrieved, and contact information obtained for comprehensive crew management."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_crew_schedule",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": 'CM008'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_68",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020, and aircraft AC003. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Aircraft status: AC003 scheduled for maintenance"
            "- Certification check: A320neo with 30-day expiry threshold"
            "- Aircraft details: B787-9 model specifications"
            "- Notes: Crew members activated, role assigned, availability verified, aircraft status updated, certification checked, and aircraft model details retrieved for comprehensive operational coordination."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_aircraft_by_model",
                kwargs={"model_id": 'B787-9'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_69",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and performance metrics need evaluation. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Performance evaluation: CM013 operational metrics retrieval"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, performance assessment for both CM008 and CM013, role promotion, aircraft maintenance scheduling, and operational performance evaluation for enhanced crew deployment efficiency."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": "CM013"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_70",
        instruction="You are a crew manager responsible for optimizing crew scheduling, operational readiness, and comprehensive airport coordination. You need to work with: crew member CM013, crew member CM020, aircraft AC003, certification type A320neo, expiry threshold days 30, role Captain, status Active, new status Active, airport ORD. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through detailed airport facility analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and airport facility coordination. The objective is to activate crew members CM013 and CM020 for operational assignments, update CM013's role to Captain, verify availability for Captain and Flight Attendant roles, schedule maintenance for aircraft AC003, verify A320neo certification status, and retrieve comprehensive ORD airport details for operational planning and crew coordination.",
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_71",
        instruction="You are a senior operations manager responsible for comprehensive flight operations and customer service management. Your role involves managing passenger reservations, ensuring flight operational efficiency, and maintaining high standards of service delivery. You need to help customer emma.jackson2892@example.com with their reservation KDBNYP. They want to get off at the connecting airport instead of the destination airport. New price of the flight that is kept should be updated to original whole cost of flight to avoid refund.",
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="update_reservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "flights": [
                        {
                            "origin": "ORD",
                            "destination": "IAH",
                            "flight_number": "HAT165",
                            "date": "2024-05-27",
                            "price": 2049
                        }
                    ]
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_72",
        instruction=(
            "You are 'operations.manager@airline.com'. Customer emma.jackson2892@example.com with reservation KDBNYP requires comprehensive reservation management and operational coordination for ORD to EWR route on May 27, 2024. You need to finalize their arrangements with the following details:\n"
            "- Customer: Emma Jackson profile verification (membership status)"
            "- Reservation: KDBNYP (current details review)"
            "- Route: ORD to EWR on May 27, 2024 (alternative flights search)"
            "- Cabin: Business class upgrade (premium service)"
            "- Insurance: Travel insurance coverage (comprehensive protection)"
            "- Baggage: 2 total bags (standard allowance)"
            "- Flight status: HAT093 operational monitoring (service verification)"
            "- Operational events: May 27, 2024 tracking (disruption awareness)"
            "- Airport: ORD facilities verification (operational coordination)"
            "- Maintenance: AC003 logs review (aircraft readiness)"
            "- Notes: Comprehensive operations management including reservation updates, flight monitoring, event tracking, and maintenance coordination for service excellence."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": "ORD", "destination": "EWR", "date": "2024-05-27"}
            ),
            Action(
                name="update_reservation",
                kwargs={"reservation_id": "KDBNYP", "cabin": "business", "insurance": "yes", "total_baggages": 2}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={"flight_number": "HAT093", "date": "2024-05-27"}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": "AC003", "start_date": "2024-05-27", "end_date": "2024-05-27"}
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_73",
        instruction=(
            "You are a senior operations manager responsible for customer service operations. You need to work with customer emma.jackson2892@example.com and manage their reservation KDBNYP. You need to finalize their arrangements with the following details:\n"
            "- Customer: emma.jackson2892@example.com (profile retrieval required)"
            "- Reservation: KDBNYP (ORD to EWR on 2024-05-27)"
            "- Flight: HAT165 (status verification needed)"
            "- Cabin class: business (upgrade required)"
            "- Insurance: yes (coverage to be added)"
            "- Baggage: 2 total baggages, 1 nonfree baggage"
            "- Route: ORD (origin) to EWR (destination)"
            "- Date: 2024-05-27"
            "- Notes: Customer profile retrieved, reservation details updated with business class upgrade, insurance added, and baggage allowance configured."
        ),       
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": "ORD", "destination": "EWR", "date": "2024-05-27"}
            ),
            Action(
                name="update_reservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "cabin": "business",
                    "insurance": "yes",
                    "total_baggages": 2,
                    "nonfree_baggages": 1
                }
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_74",
        instruction=(
            "You are 'crew.manager@airlineops.com'. Crew members CM013 need to be activated for operational assignments with role updates and home base modifications. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Availability check: Active Captains for operational assignments"
            "- Home base update: CM013 assigned to LAX airport"
            "- Aircraft status update: AC001 to Active for operational readiness"
            "- Notes: Crew members activated, role assigned, home base updated, and aircraft status verified for operational readiness."
        ),
        actions=[
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),            
            Action(
                name="update_crew_member_home_base",
                kwargs={"crew_id": 'CM013', "new_home_base": 'LAX'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC001', "new_status": 'Active'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_75",
        instruction=(
            "You are a crew manager responsible for comprehensive crew management and operational coordination. You need to handle crew members CM013 and CM020, including activation, role assignments, and contact information retrieval. Update both crew members to Active status, assign CM013 to Captain role, verify availability for Captain and Flight Attendant positions, and retrieve CM013's contact information for operational communication.\n"
            "- Crew member CM013: activation, Captain role assignment, and contact retrieval"
            "- Crew member CM020: activation for operational readiness"
            "- Status management: Active status for both crew members"
            "- Role assignments: Captain for CM013"
            "- Availability verification: Active Captain and Flight Attendant roles"
            "- Performance metrics: CM008 evaluation for crew assessment"
            "- Contact management: CM013 information for operational coordination"
            "- Notes: Comprehensive crew management including activation, role assignments, availability verification, performance evaluation, and contact information retrieval for optimal operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_76",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and A320neo certification status needs verification. Operational events coordination required for May 15-20, 2024. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 came out of maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Operational coordination: Events review for May 15-20, 2024"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, performance assessment, role promotion, aircraft maintenance scheduling, certification monitoring, and operational events coordination for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_77",
        instruction=(
            "You are 'service.manager@airline.com'. Gold tier customer mei.hernandez3561@example.com with reservation R9QDGB (LAX to BOS via SFO on 2024-05-15, flight HAT034) requires baggage enhancement processing. You need to finalize their arrangements with the following details:\n"
            "- Customer profile: Gold tier member verification for mei.hernandez3561@example.com"
            "- Reservation: R9QDGB current details review"
            "- Flight availability: LAX to SFO on 2024-05-15 verification"
            "- Flight availability: SFO to BOS on 2024-05-15 verification"
            "- Flight status: HAT034 operational readiness check"
            "- Baggage enhancement: 4 total bags with 2 non-free bags update"
            "- Reservation update: Enhanced baggage allowance processing"
            "- Final verification: Updated reservation details confirmation"
            "- Notes: Comprehensive baggage enhancement processing for gold tier customer including profile verification, reservation review, dual-leg flight availability confirmation, flight status check, baggage allowance update, and final reservation verification for optimal service coordination."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": 'mei.hernandez3561@example.com'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": 'LAX', "destination": 'SFO', "date": '2024-05-15'}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": 'SFO', "destination": 'BOS', "date": '2024-05-15'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={"flight_number": 'HAT034', "date": '2024-05-15'}
            ),
            Action(
                name="update_reservation_baggage",
                kwargs={"reservation_id": 'R9QDGB', "total_baggages": 4, "nonfree_baggages": 2}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
        ],
        outputs=["Gold tier member profile for Mei Hernandez retrieved for baggage enhancement processing", "Current reservation R9QDGB showing economy class flight from LAX to BOS via SFO on 2024-05-15", "Available flights from LAX to SFO on 2024-05-15 confirming first leg route viability", "Available flights from SFO to BOS on 2024-05-15 confirming second leg route viability", "Flight HAT034 status for May 15, 2024 showing LAX to SFO operational readiness", "Reservation R9QDGB successfully updated with 4 total bags (2 non-free) for enhanced baggage allowance", "Final reservation details showing enhanced baggage allowance for gold tier benefits"]
    ),

    Task(
        annotator="0",
        user_id="user_78",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and A320neo certification status needs verification. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Maintenance logs: AC003 historical records retrieval"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, performance assessment, role promotion, aircraft maintenance scheduling, maintenance log review, and certification monitoring for optimal operational coordination."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": "AC003"}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_79",
        instruction=(
            "You are 'crew.deployment@airline.com'. Crew members CM008 and CM012 require comprehensive management including status activation, role assignments, and performance evaluation. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM008: information retrieval for deployment planning"
            "- Crew member CM012: information retrieval and activation processing"
            "- Status management: Active status activation for CM012"
            "- Role assignment: CM008 promotion to Captain"
            "- Role assignment: CM012 assignment to Flight Attendant"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics evaluation"
            "- Notes: Comprehensive crew deployment management including dual crew information retrieval, status activation processing, strategic role assignments, multi-role availability verification, and performance evaluation for optimal airline operations coordination."
        ),       
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM012'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM012', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_profile",
                kwargs={"crew_id": 'CM008', "role": 'Captain'}
            ),
            Action(
                name="update_crew_profile",
                kwargs={"crew_id": 'CM012', "role": 'Flight Attendant'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_80",
        instruction=(
            "You are 'service.manager@airline.com'. Customer mia.li3818@example.com with reservation NO6JO3 requires first class upgrade with travel insurance for flight HAT083 on 2024-05-16. LAX airport facilities and operational events need monitoring. You need to finalize their arrangements with the following details:\n"
            "- Reservation: NO6JO3 current details retrieval"
            "- Customer profile: mia.li3818@example.com verification"
            "- Reservation upgrade: First class cabin with travel insurance"
            "- Payment processing: credit_card_4421486 method"
            "- Post-upgrade verification: Updated reservation details confirmation"
            "- Flight monitoring: HAT083 status check on 2024-05-16"
            "- Schedule coordination: Daily flight schedule for 2024-05-16"
            "- Airport assessment: LAX facilities evaluation"
            "- Operational monitoring: LAX events for 2024-05-16"
            "- Notes: Comprehensive reservation management including profile verification, first class upgrade processing, payment handling, post-upgrade verification, flight status monitoring, schedule coordination, airport facilities assessment, and operational event monitoring for superior customer experience."
        ),        
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'mia.li3818@example.com'}
            ),
            Action(
                name="update_reservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={'iata_code': 'LAX'}
            ),
            Action(
                name="get_operational_events",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'LAX'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_81",
        instruction=(
            "You are 'operations.manager@airline.com'. Customer emma.jackson2892@example.com with reservation KDBNYP (ORD to EWR via IAH on 2024-05-27) requires comprehensive flight operations management. ORD airport facilities and crew member CM013 contact information need coordination. You need to finalize their arrangements with the following details:\n"
            "- Customer profile: emma.jackson2892@example.com verification"
            "- Reservation: KDBNYP current details review"
            "- Flight search: ORD to IAH on 2024-05-27 availability check"
            "- Operational monitoring: Events assessment for 2024-05-27"
            "- Airport coordination: ORD facilities evaluation"
            "- Crew communication: CM013 contact information retrieval"
            "- Notes: Comprehensive flight operations management including customer profile verification, reservation review, flight availability search, operational events monitoring, airport facilities coordination, and crew contact information retrieval for optimal customer service and operational excellence."
        ),        
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": "emma.jackson2892@example.com"}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-27"}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": "CM013"}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_82",
        instruction=(
            "You are a crew manager responsible for comprehensive operational readiness and crew optimization. You need to manage crew members CM013 and CM020, update aircraft AC003 to Maintenance status, verify A320neo certifications within 30 days expiry, review operational events from 2024-05-15 to 2024-05-20, and retrieve CM013 contact information. Activate CM020 for operational readiness and verify availability for Captain and Flight Attendant positions.\n"
            "- Crew member CM013: information retrieval and contact retrieval"
            "- Crew member CM020: activation for operational readiness"
            "- Aircraft AC003: status scheduled for maintenance"
            "- Certification monitoring: A320neo type with 30-day expiry threshold"
            "- Operational events: review period 2024-05-15 to 2024-05-20 for coordination"
            "- Availability verification: Active Captain and Flight Attendant roles"
            "- Notes: Comprehensive operational management including crew information retrieval, crew activation, aircraft maintenance, certification monitoring, operational events review, and contact information retrieval."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20'}
            ),
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": 'CM013'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_83",
        instruction="You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM024, crew member CM012, role Captain, role Flight Attendant, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through comprehensive availability verification. You have access to manage: crew status updates, crew role assignments, and crew availability monitoring. The objective is to activate crew members CM024 and CM012 for operational assignments, update CM024's role to Captain and CM012's role to Flight Attendant, and ensure comprehensive availability verification across Captain and Flight Attendant crew categories for operational readiness and strategic crew coordination."
        ,actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM024'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM012'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM024', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM012', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_profile",
                kwargs={"crew_id": 'CM024', "role": 'Captain'}
            ),
            Action(
                name="update_crew_profile",
                kwargs={"crew_id": 'CM012', "role": 'Flight Attendant'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM024'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_84",
        instruction="You are a senior operations manager responsible for comprehensive flight operations and customer service management. You need to work with: customer chen.hernandez3740@example.com, reservation V25KYO, origin EWR, destination ORD, date 2024-05-21, end date 2024-05-21, cabin class business, insurance yes, payment method credit_card_8453507, total baggages 3, nonfree baggages 1, airport ORD, role Flight Attendant, status Active, aircraft AC003, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling while maintaining operational excellence, and ensure operational readiness through maintenance tracking. Focus on providing comprehensive operational oversight and customer service excellence across reservation lifecycle management, customer profile handling, flight search operations, schedule management, operational event monitoring, airport facilities evaluation, crew coordination, and aircraft maintenance monitoring.",
        actions=[
            Action(
                name="get_user_profile",
                kwargs={"user_email": 'chen.hernandez3740@example.com'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": 'EWR', "destination": 'ORD', "date": '2024-05-21'}
            ),

            Action(
                name="get_flight_schedule",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="update_reservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'business', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"aircraft_id": 'AC003', "start_date": '2024-05-21', "end_date": '2024-05-21'}
            )
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_85",
        instruction=(
            "You are 'crew.operations@airline.com'. Crew members CM013 and CM020 require comprehensive management including activation, role assignments, and certification compliance. CM013 needs Captain role assignment and performance evaluation. A320neo certification status requires verification. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: Captain role assignment (multiple updates required)"
            "- Crew member CM013: information retrieval for deployment planning"
            "- Crew member CM020: information retrieval for deployment planning"
            "- Status management: Active status activation for CM013"
            "- Status management: Active status activation for CM020"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM013 operational metrics evaluation"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Role assignment: CM020 assignment to Flight Attendant"
            "- Notes: Comprehensive crew operations management including repeated Captain role assignments for CM013, dual crew information retrieval, activation status management, multi-role availability verification, performance assessment, certification monitoring, and strategic role assignments for optimal operational readiness."
        ),       
        actions=[
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),            
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM020', "role": 'Flight Attendant'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_86",
        instruction=(
            "You are a crew manager responsible for comprehensive crew optimization and operational readiness. You need to manage crew members CM013 and CM020, update aircraft AC003 to Maintenance status, verify A320neo certifications within 30 days expiry, and retrieve performance metrics. Activate both crew members, assign CM013 to Captain role, verify Captain availability, and evaluate CM013 and CM008 performance.\n"
            "- Crew member CM013: activation, Captain role assignment, and performance evaluation"
            "- Crew member CM020: activation for operational readiness"
            "- Aircraft AC003: status scheduled for maintenance"
            "- Certification monitoring: A320neo type with 30-day expiry threshold"
            "- Availability verification: Active Captain role for operational planning"
            "- Performance metrics: CM008 and CM013 evaluation for crew assessment"
            "- Notes: Comprehensive operational management including crew activation, role assignments, aircraft maintenance, certification monitoring, and performance evaluation for optimal crew scheduling."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_87",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, verify availability for Captain and Flight Attendant roles, update AC003 aircraft to Maintenance status, monitor A320neo certification status with 30-day expiry threshold, review operational events from 2024-05-14 to 2024-05-19, and analyze A-Check maintenance logs for the same period.\n"
            "- Crew member CM013: information retrieval for assessment"
            "- Crew member CM020: information retrieval for assessment"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Operational events: 2024-05-14 to 2024-05-19 period review"
            "- Maintenance analysis: A-Check logs for 2024-05-14 to 2024-05-19"
            "- Notes: Comprehensive crew management including information retrieval, multi-role availability verification, aircraft maintenance, certification monitoring, operational events review, and maintenance log analysis for optimal operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-14', "end_date": '2024-05-19'}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"start_date": '2024-05-14', "end_date": '2024-05-19', "maintenance_type": 'A-Check'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_88",
        instruction="You are a crew deployment specialist responsible for comprehensive crew management and operational coordination. Your primary responsibility involves crew member information retrieval for CM013 and CM020, crew status activation for both crew members, comprehensive availability monitoring across Captain and Flight Attendant roles, crew role assignment for CM013 to Captain, aircraft status management for AC003 to Maintenance, crew certification verification for A320 aircraft with 30-day expiry threshold, maintenance log review for A-Check type from 2024-05-15 to 2024-05-20, and ORD airport facility coordination. The workflow integrates crew information gathering, status management, availability assessment, role assignment, aircraft maintenance coordination, certification monitoring, maintenance record analysis, and airport infrastructure assessment for comprehensive airline operations management. Your coordination efforts should ensure seamless crew activation, effective role assignments, thorough availability verification, proper aircraft maintenance scheduling, certification compliance, maintenance record review, and airport facility coordination for optimal operational efficiency. Key parameters: crew_id_1=CM013, crew_id_2=CM020, aircraft_id=AC003, new_status=Maintenance, certification_type=A320, expiry_threshold=30, maintenance_type=A-Check, airport_code=ORD, date_range=2024-05-15_to_2024-05-20",
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20', "maintenance_type": 'A-Check'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_89",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve information for crew members CM013 and CM020, activate both crew members for operational readiness, verify availability for Captain and Flight Attendant roles, update AC003 aircraft to Maintenance status, monitor A320neo certification status with 30-day expiry threshold, review ORD airport facilities, and retrieve CM013 contact information for operational communication.\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Active Captain role"
            "- Availability verification: Active Flight Attendant role"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Airport coordination: ORD facilities review"
            "- Contact retrieval: CM013 contact information"
            "- Notes: Comprehensive crew management including information retrieval, dual crew activation, multi-role availability verification, aircraft maintenance, certification monitoring, airport coordination, and contact information retrieval for optimal operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": 'CM013'}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_90",
        instruction=(
            "You are 'crew.manager@airline.com'. Crew members CM013 and CM020 need activation for operational assignments with CM013 promoted to Captain role. Aircraft AC003 requires maintenance scheduling and A320neo certification status needs verification. Operational events coordination required for May 15-20, 2024. You need to finalize their arrangements with the following details:\n"
            "- Crew member CM013: information retrieval and activation"
            "- Crew member CM020: information retrieval and activation"
            "- Status management: Active status for both CM013 and CM020"
            "- Availability verification: Captain role (Active status)"
            "- Performance assessment: CM008 operational metrics review"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Role assignment: CM013 promotion to Captain"
            "- Aircraft maintenance: AC003 put under maintenance"
            "- Certification monitoring: A320neo with 30-day expiry threshold"
            "- Operational coordination: Events review for May 15-20, 2024"
            "- Notes: Comprehensive crew management including dual crew information retrieval, activation status management, multi-role availability verification, performance assessment, role promotion, aircraft maintenance scheduling, certification monitoring, and operational events coordination for optimal operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_operational_events",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_91",
        instruction="You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM013, crew member CM020, certification type A320neo, expiry threshold days 30, role Captain, role Flight Attendant. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, crew certification monitoring. The objective is to activate crew members CM013 and CM020 for operational assignments, update CM013 to Captain role, verify crew availability for Captain and Flight Attendant roles, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=["Crew member CM013 (Linda Johnson) - Flight Attendant based at LAX airport, currently Inactive status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM013'", "Crew member CM020 (Patricia Johnson) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020'", "Crew members CM013 and CM020 statuses all updated to Active for operational readiness via update_crew_member_status actions", "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain' and status 'Active'", "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant' and status 'Active'", "Crew member CM013 role successfully updated to Captain for operational assignments via update_crew action with crew_id 'CM013' and role 'Captain'", "Crew certification status for A320neo aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320neo' and expiry_threshold_days 30"]
    ),
    
    Task(
        annotator="0",
        user_id="user_92",
        instruction="You are a senior operations manager responsible for customer service operations. You need to work with: reservation V25KYO, origin EWR, destination ORD, date 2024-05-21, end date 2024-05-21, cabin class first, insurance yes, payment method credit_card_8453507, total baggages 3, nonfree baggages 1, airport ORD, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling.  You have access to manage: flight status monitoring, schedule management. ",
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="find_flights",
                kwargs={"origin": 'EWR', "destination": 'ORD', "date": '2024-05-21'}
            ),

            Action(
                name="get_flight_schedule",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="update_reservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'first', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="get_airport_details_by_iata_code",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_93",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020, and aircraft AC003. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Performance check: CM008 metrics evaluation"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Aircraft status: AC003 put under maintenance"
            "- Certification check: A320neo with 30-day expiry threshold"
            "- Notes: Crew members activated, role assigned, availability verified, aircraft status updated, and certification status checked for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_94",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020, and aircraft AC003. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Performance check: CM008 metrics evaluation"
            "- Performance check: CM013 metrics evaluation"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Aircraft status: AC003 scheduled for maintenance"
            "- Notes: Crew members activated, role assigned, dual performance evaluations completed, availability verified, and aircraft status updated for operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_95",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020, and aircraft AC003. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Performance check: CM008 metrics evaluation"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Aircraft status: AC003 scheduled for maintenance"
            "- Notes: Crew members activated, role assigned, availability verified, and aircraft status updated for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
        ],
        outputs=["Crew member CM013 (Linda Johnson) - Flight Attendant based at LAX airport, currently Inactive status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM013", "Crew member CM020 (Patricia Johnson) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020", "Crew member CM013 status updated to Active, CM020 status updated to Active via update_crew_member_status actions", "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain' and status 'Active", "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant' and status 'Active", "Crew member CM013 role successfully updated to Captain for operational assignments via update_crew action with crew_id 'CM013' and role 'Captain", "Aircraft AC003 status updated to Maintenance via update_aircraft_status action with aircraft_id 'AC003' and new_status 'Maintenance"]
    ),
    
    Task(
        annotator="0",
        user_id="user_96",
        instruction=(
            "You are 'crew.manager@airline.com' responsible for comprehensive crew management and operational coordination. You need to retrieve contact information and member details for CM008, get member information for CM012, activate CM012 for operational readiness, assign CM008 to Captain role, assign CM012 to Flight Attendant role, verify availability for both Captain and Flight Attendant roles, and assess CM008 performance metrics.\n"
            "- Crew member CM008: contact info retrieval and member details"
            "- Crew member CM012: member information retrieval and activation"
            "- Status management: CM012 activation to Active status"
            "- Role assignment: Captain role for CM008"
            "- Role assignment: Flight Attendant role for CM012"
            "- Availability verification: Active Captain role status"
            "- Availability verification: Active Flight Attendant role status"
            "- Performance assessment: CM008 metrics evaluation"
            "- Notes: Comprehensive crew management including contact information retrieval, member information gathering, status activation, dual role assignments, multi-role availability verification, and performance metrics assessment for optimal operational readiness."
        ),
        actions=[
            Action(
                name="get_crew_contact_info",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM012'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM012', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_profile",
                kwargs={"crew_id": 'CM008', "role": 'Captain'}
            ),
            Action(
                name="update_crew_profile",
                kwargs={"crew_id": 'CM012', "role": 'Flight Attendant'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_97",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020, and aircraft AC003. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Performance check: CM013 metrics evaluation"
            "- Performance check: CM008 metrics evaluation"
            "- Availability verification: Captain role (Active status)"
            "- Availability verification: Flight Attendant role (Active status)"
            "- Aircraft status: AC003 put under maintenance"
            "- Notes: Crew members activated, role assigned, dual performance evaluations completed, availability verified, and aircraft status updated for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'In Maintenance'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_98",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020, and aircraft AC003. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (information retrieval)"
            "- Crew member: CM020 (status update to Active)"
            "- Aircraft status: AC003 scheduled for maintenance"
            "- Certification check: A320neo with 30-day expiry threshold"
            "- Maintenance review: A-Check type from 2024-05-15 to 2024-05-20"
            "- Status management: CM020 activation for operational readiness"
            "- Aircraft coordination: AC003 maintenance scheduling"
            "- Notes: Crew member information retrieved, CM020 activated, aircraft status updated, certification checked, and maintenance logs reviewed for operational readiness."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance Scheduled'}
            ),
            Action(
                name="get_crew_certification_status",
                kwargs={"certification_type": 'A320neo', "expiry_threshold_days": 30}
            ),
            Action(
                name="get_maintenance_logs",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20', "maintenance_type": 'A-Check'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_99",
        instruction=(
            "You are a crew manager responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM013 and CM020. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM013 (status update to Active)"
            "- Crew member: CM020 (status update to Active)"
            "- Role assignment: CM013 promoted to Captain"
            "- Performance check: CM008 metrics evaluation"
            "- Availability verification: Captain role (Active status)"
            "- Status management: Dual crew activation for operational readiness"
            "- Role coordination: Captain leadership assignment"
            "- Notes: Crew members activated, role assigned, performance evaluated, and availability verified for comprehensive crew management."
        ),        
        actions=[
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="get_crew_member_info",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="update_crew_member_status",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="get_crew_availability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="get_crew_performance_metrics",
                kwargs={"crew_id": 'CM008'}
            ),            
            Action(
                name="update_crew",
                kwargs={"crew_id": 'CM013', "role": 'Captain'}
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_100",
        instruction=(
            "You are a senior operations manager responsible for customer service operations and baggage management. You need to work with customer mia.li3818@example.com and manage their reservation NO6JO3. You need to finalize their arrangements with the following details:\n"
            "- Customer: mia.li3818@example.com (profile retrieval required)"
            "- Reservation: NO6JO3 (details retrieval and updates)"
            "- Cabin class: first (upgrade required)"
            "- Insurance: yes (coverage to be added)"
            "- Payment method: credit_card_4421486 (for reservation processing)"
            "- Flight: HAT083 (status verification for 2024-05-16)"
            "- Schedule review: 2024-05-16 flight operations"
            "- Baggage: 3 total baggages (update required)"
            "- Notes: Customer profile retrieved, reservation upgraded to first class with insurance, flight status verified, schedule reviewed, and baggage updated for enhanced service management."
        ),        
        actions=[
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_user_profile",
                kwargs={'user_email': 'mia.li3818@example.com'}
            ),
            Action(
                name="update_reservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="get_reservation_details",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="get_flight_status_by_number_and_date",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="get_flight_schedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="update_reservation_baggage",
                kwargs={'reservation_id': 'NO6JO3', 'total_baggages': 3}
            ),
        ],
        outputs=[]
    ),
] 