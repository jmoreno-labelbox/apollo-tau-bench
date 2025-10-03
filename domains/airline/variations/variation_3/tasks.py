from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="user_1",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through aircraft coordination. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status updates. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification for Captain roles, update CM015's role to Captain, and schedule maintenance for aircraft AC003.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions with crew_member_id 'CM015' and 'CM020', new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for operational readiness and maintenance scheduling"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_2",
        instruction="Execute senior operations management responsible for comprehensive customer service operations and flight management. A customer has an existing reservation NO6JO3 that needs to be upgraded to FIRST class with travel insurance using payment method credit_card_4421486. You need to verify the current reservation details, access the customer profile for service history, process the upgrade according to airline policies, monitor the operational status of the customer's flight, review the daily flight schedule for operational coordination, and identify alternative flight options from JFK to ORD for potential rebooking needs. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, and provide comprehensive flight search capabilities for route planning and customer flexibility. You have access to manage: reservation lifecycle management, customer profile handling, flight status monitoring, schedule management, and flight search operations.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetUserProfile",
                kwargs={'user_email': 'emma.smith8074@example.com'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="FindFlights",
                kwargs={'origin': 'JFK', 'destination': 'ORD', 'date': '2024-05-16', 'cabin_class': 'business'}
            ),
        ],
        outputs={
            "customer_profile": "Customer profile retrieved for service history and membership level evaluation",
            "reservation_details": "Current reservation details verified before processing upgrade",
            "reservation_update": "Reservation successfully upgraded to FIRST class with travel insurance according to airline policies",
            "reservation_confirmation": "Updated reservation details confirmed after upgrade processing",
            "flight_status": "Operational status of customer's flight monitored for service coordination",
            "daily_schedule": "Daily flight schedule reviewed for operational coordination and planning",
            "flight_search": "Available business class flights from JFK to ORD on May 16, 2024 identified for potential rebooking options and customer flexibility"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_3",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, origin ORD, destination IAH, date 2024-05-27, cabin class business, insurance yes, total baggages 2, flight HAT083, airport ORD. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, maintain operational awareness through flight status monitoring, ensure operational excellence through event tracking, enhance operational coordination through airport facilities evaluation, and ensure operational readiness through maintenance tracking. You have access to manage: reservation lifecycle management, customer profile handling, flight search operations, flight status monitoring, operational event assessment, airport facilities coordination, and aircraft maintenance monitoring. The objective is to retrieve customer profile information for sophia.santos7908@example.com, get current reservation details for KDBNYP, find available flights from ORD to IAH on 2024-05-27, update reservation KDBNYP with business class, insurance, and 2 baggages without modifying the existing payment method, confirm updated reservation details, get flight status for HAT083 on 2024-05-27, retrieve operational events for 2024-05-27, get airport details for ORD, and get maintenance logs for aircraft AC003 on 2024-05-27 to ensure comprehensive operational coordination and customer service excellence.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-27"}
            ),
            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "cabin": "business",
                    "insurance": "yes",
                    "total_baggages": 2
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT083", "date": "2024-05-27"}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": "AC003", "start_date": "2024-05-27", "end_date": "2024-05-27"}
            )
        ],
        outputs={
            "customer_profile": "Olivia Santos gold tier member profile with membership benefits retrieved via get_user_profile with user_email 'sophia.santos7908@example.com' for service assessment",
            "reservation_details": "Current reservation KDBNYP details showing ORD to IAH routing in business class retrieved via get_reservation_details with reservation_id 'KDBNYP' for reservation management",
            "alternative_flights": "Available alternative flights from ORD to IAH on May 27, 2024 retrieved via find_flights with origin 'ORD', destination 'IAH', date '2024-05-27' for rebooking options and route flexibility",
            "reservation_update": "Updated reservation KDBNYP with cabin class business, insurance yes, total_baggages: 2 via update_reservation with reservation_id 'KDBNYP', cabin 'business', insurance 'yes', total_baggages 2 without modifying existing payment method according to customer requirements",
            "reservation_confirmation": "Confirmed reservation details after updates retrieved via get_reservation_details with reservation_id 'KDBNYP' showing business class cabin, insurance coverage, and baggage allowance",
            "flight_status": "Flight HAT083 status for May 27, 2024 retrieved via get_flight_status_by_number_and_date with flight_number 'HAT083', date '2024-05-27' showing operational details and availability",
            "operational_events": "Operational events and disruptions for May 27, 2024 retrieved via get_operational_events with start_date '2024-05-27', end_date '2024-05-27' showing delays, weather impacts, and technical issues affecting flight operations",
            "airport_facilities": "Chicago O'Hare International Airport (ORD) facilities and operational details retrieved via get_airport_details_by_iata_code with iata_code 'ORD' showing terminal information, services, and ground operations capabilities",
            "maintenance_logs": "Maintenance logs for aircraft AC003 on May 27, 2024 retrieved via get_maintenance_logs with aircraft_id 'AC003', start_date '2024-05-27', end_date '2024-05-27' showing maintenance activities, issues, and operational readiness status"
        }
    ),

    Task(
        annotator="0",
        user_id="user_4",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. Your role involves overseeing passenger reservations, ensuring flight operational efficiency, and maintaining high standards of service delivery across all operational aspects. You need to address a customer service scenario involving reservation upgrades, flight availability assessment, and operational coordination. Your responsibilities include: managing customer profiles and reservation changes according to airline policies, evaluating flight options and availability for optimal routing, monitoring flight status and operational conditions, assessing operational events that may impact service quality, coordinating with airport facilities for smooth operations, ensuring aircraft readiness and maintenance status, and verifying crew assignments for operational efficiency. You have access to tools for reservation management, customer service coordination, flight operations monitoring, aircraft management, and crew oversight.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetUserProfile",
                kwargs={'user_email': 'emma.smith8074@example.com'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'ORD'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={'iata_code': 'ORD'}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={'model_id': 'B737-800'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={'crew_id': 'CM001'}
            ),
        ],
        outputs={
            "customer_profile": "Isabella Brown's customer profile including membership level, payment methods, and reservation history for NO6JO3",
            "reservation_details": "Current reservation NO6JO3 details retrieved before update",
            "reservation_update": "Reservation NO6JO3 successfully upgraded to first class with travel insurance, showing updated cabin class, insurance status, and payment method",
            "reservation_confirmation": "Updated reservation NO6JO3 details confirmed after changes",
            "flight_status": "Flight HAT083 status for May 16, 2024 showing operational details, origin/destination, scheduled times, and availability",
            "daily_schedule": "Flight schedule summary for May 16, 2024 showing total flights, key operations, and coordination opportunities across the network",
            "operational_events": "Operational events and disruptions at ORD airport on May 16, 2024 showing delays, weather impacts, and technical issues affecting flight operations",
            "airport_facilities": "Chicago O'Hare International Airport (ORD) facilities and operational details showing terminal information, services, and ground operations capabilities",
            "aircraft_model_info": "Aircraft model B737-800 information showing manufacturer, capacity, range, and technical specifications for fleet planning",
            "crew_member_info": "Crew member CM001 details showing role, status, flight experience, and operational qualifications for crew management"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_5",
        instruction="Execute senior operations management responsible for comprehensive customer service operations and flight management. You need to work with: reservation NO6JO3, customer emma.smith8074@example.com, cabin class first, insurance yes, payment method credit_card_4421486, flight HAT083, date 2024-05-16, start date 2024-05-16, end date 2024-05-16, airport ORD, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through complete reservation lifecycle management, ensure efficient flight operations and strategic scheduling, provide operational awareness through event monitoring, and handle reservation modifications including cancellations. You have access to manage: reservation lifecycle management, customer profile handling, flight status monitoring, schedule management, and operational event tracking. The objective is to get reservation details for NO6JO3, get customer profile for emma.smith8074@example.com, update reservation NO6JO3 to first class with insurance and payment method credit_card_4421486, confirm the updated reservation details, get flight status for HAT083 on 2024-05-16, get flight schedule for 2024-05-16, cancel reservation NO6JO3 after upgrade completion, and get operational events at ORD airport on 2024-05-16.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetUserProfile",
                kwargs={'user_email': 'emma.smith8074@example.com'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="CancelReservation",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'ORD'}
            ),
        ],
        outputs={
            "customer_profile": "Isabella Brown's customer profile including membership level, payment methods, and reservation history for NO6JO3",
            "reservation_update": "Reservation NO6JO3 successfully upgraded to first class with travel insurance, showing updated cabin class, insurance status, and payment method",
            "flight_status": "Flight HAT083 status for May 16, 2024 showing operational details, origin/destination, scheduled times, and availability",
            "daily_schedule": "Flight schedule summary for May 16, 2024 showing total flights, key operations, and coordination opportunities across the network",
            "reservation_cancellation": "Reservation NO6JO3 cancellation processed with refund details and confirmation status",
            "operational_events": "Operational events and disruptions at ORD airport on May 16, 2024 showing delays, weather impacts, and technical issues affecting flight operations"
        }
    ),

    Task(
        annotator="0",
        user_id="user_6",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. Your role involves strategic oversight of crew assignments, aircraft maintenance coordination, and ensuring compliance with airline policies and safety regulations. You need to address operational scenarios involving crew activation, role assignments, and maintenance scheduling while maintaining comprehensive visibility into crew availability across all operational categories. Your responsibilities include: managing crew member activations and status changes according to operational requirements, assigning crew roles based on qualifications and operational needs, coordinating aircraft maintenance schedules to minimize operational disruption, monitoring crew availability across all role categories for optimal resource allocation, verifying crew certification compliance with regulatory requirements, and reviewing maintenance history to ensure aircraft operational readiness. You have access to tools for crew management, aircraft coordination, certification verification, and maintenance oversight.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": 'AC003'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'First Officer', "status": 'Active'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),

    Task(
        annotator="0",
        user_id="user_7",
        instruction="Execute senior operations management responsible for reservation management and customer service. You need to work with: reservation UX0R03, customer fatima.johnson5264@example.com, flights HAT289 and HAT135 on 2024-05-22 from ORD to PHL to LGA, cabin class first, insurance yes, payment method credit_card_7872117. Your goals are to: retrieve reservation details for UX0R03, get customer profile for fatima.johnson5264@example.com, update reservation UX0R03 to upgrade flights to first class with travel insurance using payment method credit_card_7872117, and verify the updated reservation details. You have access to tools for managing reservations and customer profiles.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'UX0R03'}
            ),
            Action(
                name="GetUserProfile",
                kwargs={'user_email': 'fatima.johnson5264@example.com'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={'reservation_id': 'UX0R03', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_7872117', 'flights': [{'origin': 'ORD', 'destination': 'PHL', 'flight_number': 'HAT289', 'date': '2024-05-22', 'price': 1543}, {'origin': 'PHL', 'destination': 'LGA', 'flight_number': 'HAT135', 'date': '2024-05-22', 'price': 1404}]}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'UX0R03'}
            ),
        ],
        outputs={
            "initial_reservation": "Initial reservation details for UX0R03 showing current booking information before any modifications",
            "customer_profile": "Olivia Johnson's customer profile including membership level, payment methods, and reservation history",
            "reservation_update": "Reservation UX0R03 successfully upgraded to first class with travel insurance, showing updated cabin class, insurance status, and payment method",
            "updated_reservation": "Updated reservation details for UX0R03 confirming the first class upgrade and travel insurance addition"
        }
    ),

    Task(
        annotator="0",
        user_id="user_8",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through aircraft coordination. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status updates. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification for Captain roles, update CM015's role to Captain, and schedule maintenance for aircraft AC003.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions with crew_member_id 'CM015' and 'CM020', new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for operational readiness and maintenance scheduling"
        }
    ),

    Task(
        annotator="0",
        user_id="user_9",
        instruction="Execute senior crew operations management responsible for comprehensive crew management, aircraft maintenance coordination, and airport facility evaluation. You need to work with: crew member CM015 (Olivia Johnson) based at ORD airport, crew member CM020 (Mohamed Lopez) based at CLT airport, aircraft AC003 (B787-9 Dreamliner), O'Hare International Airport (ORD), certification type A320, expiry threshold days 30, role Captain, status Active. Your goals are to: ensure optimal crew placement and operational readiness, maintain service quality standards through strategic crew management, coordinate aircraft maintenance scheduling, and evaluate airport facilities for crew base operations. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and airport facility assessment. The objective is to activate crew members CM015 and CM020 for operational assignments, update CM015's role to Captain, schedule maintenance for aircraft AC003, verify A320 certification status, and assess ORD airport capabilities for crew operations.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "ord_airport_details": "O'Hare International Airport (ORD) facilities and operational details showing terminal information, services, and ground operations capabilities for crew base operations"
        }
    ),
        
    Task(
        annotator="0",
        user_id="user_10",
        instruction="Manage crew operations responsible for updating crew member information and monitoring crew availability. You need to work with: crew member CM008 and crew member CM012. Your need to update crew member role information and verify crew availability for operational readiness. You have access to manage: crew role assignments and crew availability monitoring. Update CM008 role to Captain and CM012 role to Flight Attendant.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM012'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM012', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM008', "role": 'Captain'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM012', "role": 'Flight Attendant'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
        ],
        outputs={
            "crew_details_8": "Crew member CM008 (Olivia Johnson) - First Officer based at LAS airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_12": "Crew member CM012 (Elizabeth Brown) - First Officer based at MCO airport, currently Inactive status, with flight experience on A320 aircraft",
            "crew_status_update": "Crew member CM012 status updated from Inactive to Active",
            "crew_role_updates": "Crew member CM008 role updated to Captain, CM012 role updated to Flight Attendant",
            "crew_availability": "Current availability of active Flight Attendant crew members for operational assignments",
        }
    ),

    Task(
        annotator="0",
        user_id="user_11",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, origin ORD, destination EWR via IAH, date 2024-05-01, cabin class business, insurance yes, total baggages 2, flight HAT165, airport ORD, aircraft AC003. Your goals are to: optimize customer experience through reservation management, ensure flight operational efficiency, maintain situational awareness of flight operations, monitor operational events for service quality, coordinate airport facilities for smooth operations, and ensure aircraft maintenance readiness. You have access to tools for managing customer profiles, reservations, flight operations, status monitoring, event assessment, facilities coordination, and maintenance tracking.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-01"}
            ),
            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "cabin": "business",
                    "insurance": "yes",
                    "total_baggages": 2
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT083", "date": "2024-05-27"}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": "AC003", "start_date": "2024-05-27", "end_date": "2024-05-27"}
            )
        ],
        outputs={
            "customer_profile": "Olivia Santos gold tier member profile with membership benefits retrieved for service assessment",
            "reservation_details": "Current reservation KDBNYP details showing ORD to EWR via IAH routing in business class",
            "alternative_flights": "Available alternative flights from ORD to IAH on May 1, 2024 for rebooking options and route flexibility",
            "reservation_update": "Updated reservation with cabin class business, insurance yes, total_baggages: 2 according to customer requirements",
            "reservation_confirmation": "Confirmed reservation details after updates showing business class cabin, insurance coverage, and baggage allowance",
            "flight_status": "Flight HAT165 status for May 1, 2024 showing operational details, ORD to IAH route, scheduled times, and availability",
            "operational_events": "Operational events and disruptions for May 1, 2024 showing delays, weather impacts, and technical issues affecting flight operations",
            "airport_facilities": "Chicago O'Hare International Airport (ORD) facilities and operational details showing terminal information, services, and ground operations capabilities",
            "maintenance_logs": "Maintenance logs for aircraft AC003 on May 1, 2024 showing maintenance activities, issues, and operational readiness status"
        }
    ),

    Task(
        annotator="0",
        user_id="user_12",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, and verify A320 certification status.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_13",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. Your role involves overseeing passenger reservations, ensuring flight operational efficiency, and maintaining high standards of service delivery across all operational aspects. You need to address a customer service scenario involving reservation upgrades, flight availability assessment, and operational coordination. Your responsibilities include: managing customer profiles and reservation changes according to airline policies, evaluating flight options and availability for optimal routing, monitoring flight status and operational conditions, assessing operational events that may impact service quality, coordinating with airport facilities for smooth operations, ensuring aircraft readiness and maintenance status, and verifying crew assignments for operational efficiency. You have access to tools for reservation management, customer service coordination, flight operations monitoring, aircraft management, and crew oversight.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetUserProfile",
                kwargs={'user_email': 'emma.smith8074@example.com'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'ORD'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={'iata_code': 'ORD'}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={'model_id': 'B737-800'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={'crew_id': 'CM001'}
            ),
        ],
        outputs={
            "customer_profile": "Isabella Brown's customer profile including membership level, payment methods, and reservation history for NO6JO3",
            "reservation_details": "Current reservation NO6JO3 details retrieved before update",
            "reservation_update": "Reservation NO6JO3 successfully upgraded to first class with travel insurance, showing updated cabin class, insurance status, and payment method",
            "reservation_confirmation": "Updated reservation NO6JO3 details confirmed after changes",
            "flight_status": "Flight HAT083 status for May 16, 2024 showing operational details, origin/destination, scheduled times, and availability",
            "daily_schedule": "Flight schedule summary for May 16, 2024 showing total flights, key operations, and coordination opportunities across the network",
            "operational_events": "Operational events and disruptions at ORD airport on May 16, 2024 showing delays, weather impacts, and technical issues affecting flight operations",
            "airport_facilities": "Chicago O'Hare International Airport (ORD) facilities and operational details showing terminal information, services, and ground operations capabilities",
            "aircraft_model_info": "Aircraft model B737-800 information showing manufacturer, capacity, range, and technical specifications for fleet planning",
            "crew_member_info": "Crew member CM001 details showing role, status, flight experience, and operational qualifications for crew management"
        }
    ),

    Task(
        annotator="0",
        user_id="user_14",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, update aircraft AC003 status to Maintenance, and verify A320 certification status.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),
    Task(
        annotator="0",
        user_id="user_15",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status updates. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, and update aircraft AC003 status to Maintenance.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance"
        }
    ),
    Task(
        annotator="0",
        user_id="user_16",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft ID AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through comprehensive maintenance oversight. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and maintenance log monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003 (using aircraft ID AC003), verify A320 certification status, and review maintenance logs for aircraft AC003 (using aircraft ID AC003) to ensure operational readiness and maintenance coordination.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": 'AC003'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "maintenance_records": "Maintenance logs for aircraft AC003 retrieved via get_maintenance_logs with aircraft_id 'AC003' showing maintenance history, current status, and operational readiness indicators for comprehensive maintenance oversight and operational coordination"
        }
    ),
    Task(
        annotator="0",
        user_id="user_17",
        instruction="You are a comprehensive crew operations manager responsible for optimizing crew scheduling, operational readiness, and flight coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active, date range 2024-01-15 to 2024-01-20, airport ORD. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, enhance flight scheduling coordination, and improve airport facility awareness for operational planning. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, flight schedule retrieval, and airport facility information. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, verify A320 certification status, retrieve flight schedules for the January 15-20, 2024 period to support crew scheduling decisions, and obtain ORD airport facility information to enhance operational planning and crew coordination.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": '2024-01-15', "end_date": '2024-01-20'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015'",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020'",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain' and status 'Active'",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant' and status 'Active'",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew action with crew_id 'CM015' and role 'Captain'",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status action with aircraft_id 'AC003' and new_status 'Maintenance'",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320' and expiry_threshold_days 30",
            "flight_schedules": "Flight schedules retrieved for date range 2024-01-15 to 2024-01-20 via get_flight_schedule action showing flight operations, aircraft assignments, and scheduling information for crew coordination and operational planning",
            "airport_facilities": "ORD airport facility information retrieved via get_airport_details_by_iata_code action with iata_code 'ORD' showing airport infrastructure, services, and operational capabilities for enhanced crew coordination and operational planning"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_18",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, and verify A320 certification status.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),

    Task(
        annotator="0",
        user_id="user_19",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, crew member CM003, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance crew coordination through comprehensive member integration. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and crew member coordination. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, verify A320 certification status, and coordinate with crew member CM003 for enhanced operational readiness and crew management integration.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM003'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "crew_details_03": "Crew member CM003 (Mohamed Lopez) - Flight Attendant based at ORD airport, currently Active status, with flight experience on A320neo aircraft for enhanced crew coordination and operational readiness"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_20",
        instruction="You are a customer service operations specialist managing comprehensive account services for sophia.santos7908@example.com. Your responsibilities include handling reservation KDBNYP (cancellation and details), finding alternative flights from ORD to IAH on 2024-05-27, monitoring flight HAT165 status, coordinating ORD airport facilities, managing flight schedules for 2024-05-27, upgrading membership from gold to platinum, and checking AC003 aircraft maintenance logs. You have access to tools for customer profile management, reservation lifecycle handling, flight search operations, flight status monitoring, airport facilities coordination, flight schedule management, membership updates.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="CancelReservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-27"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="UpdateUserMembership",
                kwargs={"user_email": "sophia.santos7908@example.com", "new_membership": "platinum"}
            ),
        ],
        outputs=[
            "user_profile_retrieved:sophia.santos7908@example.com",
            "reservation_details_retrieved:KDBNYP",
            "reservation_cancelled:KDBNYP",
            "flights_found:ORD:IAH:2024-05-27",
            "flight_status_checked:HAT165:2024-05-27",
            "airport_details_retrieved:ORD",
            "flight_schedule_retrieved:2024-05-27",
            "membership_updated:sophia.santos7908@example.com:platinum",
        ]
    ),
    
    Task(
        annotator="0",
        user_id="user_21",
        instruction="Execute senior operations management responsible for comprehensive customer service operations, crew coordination, and operational management. A customer needs to cancel their reservation due to operational requirements, and you need to coordinate this with flight operations, crew readiness, and aircraft maintenance. You must verify the customer's profile and reservation details, process the cancellation according to airline policies, monitor the operational status of the affected flight, evaluate airport facilities for operational coordination, review the daily flight schedule for strategic planning, assess crew member qualifications and certification status for operational readiness, analyze aircraft model specifications for operational planning, monitor operational events for potential disruptions, and review maintenance logs for aircraft serviceability. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, enhance operational coordination through crew member integration, optimize operational readiness through comprehensive aircraft and certification analysis, and ensure maintenance coordination through detailed aircraft maintenance analysis. You have access to manage: reservation lifecycle management, customer profile handling, flight status monitoring, airport facilities evaluation, schedule management, crew member coordination, aircraft model analysis, crew certification management, operational events monitoring, and maintenance logs coordination.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="CancelReservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),

            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={"model_id": "B737-800"}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": "B737-800", "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": "AC004"}
            ),
        ],
        outputs={
            "customer_profile": "Customer profile retrieved for service history and membership evaluation",
            "reservation_details": "Current reservation details verified before cancellation processing",
            "cancellation_result": "Reservation successfully cancelled according to airline policies with refund processing confirmation",
            "flight_status": "Operational status of affected flight monitored for coordination and planning",
            "airport_facilities": "Airport facilities evaluated for operational coordination and ground operations support",
            "daily_schedule": "Daily flight schedule reviewed for strategic operational planning and coordination",
            "crew_member_details": "Crew member qualifications and experience assessed for operational readiness",
            "aircraft_model_info": "Aircraft model specifications analyzed for operational planning and coordination",
            "crew_certifications": "B737-800 crew certification status verified with expiry assessment for operational compliance",
            "operational_events": "Operational events monitored for potential disruptions and coordination needs",
            "maintenance_logs": "Aircraft maintenance logs reviewed for serviceability and operational readiness"
        }
    ),
    Task(
        annotator="0",
        user_id="user_22",
        instruction="Execute senior operations management responsible for customer service operations, crew coordination, and comprehensive operational management. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, flight HAT165, date 2024-05-27, airport ORD, start date 2024-05-27, end date 2024-05-27, crew member CM001, aircraft model B737-800, certification type B737, expiry threshold days 30. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, enhance operational coordination through crew member integration, and optimize operational readiness through comprehensive aircraft and certification analysis. You have access to manage: flight status monitoring, schedule management, crew member coordination, aircraft model coordination, and crew certification management. The objective is to retrieve customer profile for Olivia Santos, review reservation KDBNYP details, process reservation cancellation, monitor flight HAT165 status for operational coordination, evaluate ORD airport facilities, review daily flight schedule for strategic planning, coordinate with crew member CM001 for enhanced operational readiness, retrieve detailed B737-800 aircraft model specifications for operational planning, and verify B737 crew certification status for comprehensive operational management.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="CancelReservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),

            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={"model_id": "B737-800"}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": "B737", "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "customer_profile": "Olivia Santos's gold tier member profile retrieved via get_user_profile with user_email 'sophia.santos7908@example.com' showing membership benefits and account information for customer service operations",
            "reservation_details": "Current reservation KDBNYP details retrieved via get_reservation_details with reservation_id 'KDBNYP' showing business class flight from ORD to EWR for strategic reservation management",
            "cancellation_result": "Reservation KDBNYP cancellation confirmation showing successful cancellation status and refund processing details via cancel_reservation with reservation_id 'KDBNYP' for customer service operations",
            "flight_status": "Flight HAT165 status for May 27, 2024 from ORD to IAH retrieved via get_flight_status_by_number_and_date with flight_number 'HAT165', date '2024-05-27' for flight operations monitoring",
            "airport_facilities": "O'Hare International Airport facilities and maintenance support infrastructure details retrieved via get_airport_details_by_iata_code with iata_code 'ORD' for operational coordination",
            "daily_schedule": "Complete flight schedule for 2024-05-27 showing all airline operations and available flights across the network retrieved via get_flight_schedule with start_date '2024-05-27', end_date '2024-05-27' for schedule management",
            "crew_member_details": "Crew member CM001 (Isabella Brown) - Captain based at ATL airport, currently Active status, with flight experience on B737-800 aircraft retrieved via get_crew_member_info with crew_id 'CM001' for crew coordination and operational readiness",
            "aircraft_model_info": "Aircraft B737-800 model specifications retrieved via get_aircraft_model_info with model_id 'B737-800' for comprehensive operational planning and aircraft coordination",
            "crew_certifications": "Crew certification status for B737 aircraft showing certification details and expiry information retrieved via get_crew_certification_status with certification_type 'B737', expiry_threshold_days 30 for crew certification management"
        }
    ),
    Task(
        annotator="0",
        user_id="user_23",
        instruction="Manage crew operations responsible for optimizing crew scheduling. For crew members CM010 and CM021, activate them for operational assignments and update CM010's role to Captain. Assess crew availability across all categories and verify B737 certification status. Make right crew management decisions to ensure operational efficiency.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM010'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM021'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM010', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM021', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM010', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B737'}
            ),
        ],
        outputs={
            "crew_details_10": "Crew member CM010 information and current status",
            "crew_details_21": "Crew member CM021 information and current status",
            "crew_updates": "Status updates for both crew members",
            "crew_availability_captains": "Current availability of active Captain crew members",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members",
            "crew_assignment": "CM010 role update confirmation",
            "crew_certifications": "B737 certification status for crew members"
        }
    ),
    Task(
        annotator="0",
        user_id="user_24",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. For crew members CM016 and CM018, activate them for operational assignments and update CM016's role to Captain. Assess crew availability across all categories and verify B737 certification status. Make strategic crew management decisions to ensure operational efficiency and get aircraft model information.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM016'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM018'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM016', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM018', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM016', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B737'}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={"model_id": 'B737-800'}
            ),
        ],
        outputs={
            "crew_details_16": "Crew member CM016 information and current status",
            "crew_details_18": "Crew member CM018 information and current status", 
            "crew_updates": "Status updates for both crew members",
            "crew_availability_captains": "Current availability of active Captain crew members",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members",
            "crew_assignment": "CM016 role update confirmation",
            "crew_certifications": "B737 certification status for crew members",
            "aircraft_model_info": "B737-800 aircraft model specifications and operational details"
        }
    ),

    Task(
        annotator="0",
        user_id="user_25",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status management. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, and schedule maintenance for aircraft AC003."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance scheduling"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_26",
        instruction="Manage crew operations responsible for optimizing crew info. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-15, end date 2024-05-20. Your goals are to: ensure correct crew info for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review operational events within the specified window.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-15 to 2024-05-20 showing coordination requirements"
        }
    ),
    Task(
        annotator="0",
        user_id="user_27",
        instruction="You are a comprehensive crew operations manager responsible for optimizing crew scheduling, operational readiness, and maintenance oversight. For crew members CM010 and CM021, activate them for operational assignments and update CM010's role to Captain. Assess crew availability across all categories and verify B737 certification status. Review maintenance logs for aircraft AC003 to ensure operational readiness and maintenance coordination. Make strategic crew management decisions to ensure operational efficiency while maintaining comprehensive maintenance awareness for flight safety and operational continuity.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM010'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM021'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM010', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM021', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM010', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B737'}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": 'AC003'}
            ),
        ],
        outputs={
            "crew_details_10": "Crew member CM010 information and current status",
            "crew_details_21": "Crew member CM021 information and current status",
            "crew_updates": "Status updates for both crew members",
            "crew_availability_captains": "Current availability of active Captain crew members",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members",
            "crew_assignment": "CM010 role update confirmation to Captain via update_crew action with crew_id 'CM010' and role 'Captain'",
            "crew_certifications": "B737 certification status for crew members retrieved via get_crew_certification_status with certification_type 'B737'",
            "maintenance_records": "Maintenance logs for aircraft AC003 retrieved via get_maintenance_logs with aircraft_id 'AC003' showing maintenance history, current status, and operational readiness indicators for comprehensive maintenance oversight and operational coordination"
        }
    ),

    Task(
        annotator="0",
        user_id="user_28",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, status Active, new status Active, aircraft AC003 maintenance logs. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through comprehensive maintenance oversight. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, and maintenance log monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, and review maintenance logs for aircraft AC003 to ensure operational readiness and maintenance coordination."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": 'AC003'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for operational coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for operational planning",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew management",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive crew coordination",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for optimal crew placement",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance coordination",
            "maintenance_records": "Maintenance logs for aircraft AC003 retrieved via get_maintenance_logs with aircraft_id 'AC003' showing maintenance history, current status, and operational readiness indicators for comprehensive maintenance oversight and operational coordination"
        }
    ),
    

    Task(
        annotator="0",
        user_id="user_29",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            )
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),
    Task(
        annotator="0",
        user_id="user_30",
        instruction="You are a crew management specialist responsible for coordinating comprehensive crew operations and deployment optimization. Your primary responsibility involves crew member activation and status management for CM004 and CM008, crew role assignment updates for CM004 to Captain position, crew availability monitoring across Captain and Flight Attendant roles, crew certification verification for B737 aircraft, and home base optimization for CM004 to DFW location. The workflow integrates crew information retrieval, status activation, role assignment, availability assessment, certification verification, and strategic home base deployment for optimal crew management efficiency. Your coordination efforts should ensure seamless crew activation through proper status updates, effective role assignments, comprehensive availability monitoring, thorough certification verification, and strategic home base optimization for successful airline operations management. Key parameters: crew_id_1=CM004, crew_id_2=CM008, new_status=Active, role_1=Captain, role_2=Flight_Attendant, certification_type=B737, new_home_base=DFW",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM004'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM004', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM008', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM004', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B737'}
            ),
            Action(
                name="UpdateCrewMemberHomeBase",
                kwargs={"crew_id": 'CM004', "new_home_base": 'DFW'}
            ),
        ],
        outputs=[
            "crew_member_info_retrieved:CM004",
            "crew_member_info_retrieved:CM008",
            "crew_status_updated:CM004:Active",
            "crew_status_updated:CM008:Active",
            "crew_availability_checked:Captain",
            "crew_availability_checked:Flight_Attendant",
            "crew_role_updated:CM004:Captain",
            "crew_certifications_verified:B737",
            "crew_home_base_updated:CM004:DFW"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_31",
        instruction="Execute senior operations management responsible for customer service operations. You need to work with: customer evelyn.wilson9461@example.com, reservation V25KYO, cabin class first, insurance yes, payment method credit_card_8453507, total baggages 3, nonfree baggages 1, origin EWR, destination LGA, date 2024-05-21, crew role Flight Attendant, status Active, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling. You have access to manage: flight status monitoring, schedule management, operational coordination, crew availability monitoring. The objective is to upgrade customer reservation V25KYO to first class with insurance and baggage modifications, verify the reservation update, review flight operations and schedule for operational coordination, assess operational events for potential disruptions, evaluate airport facilities for operational readiness, and assess crew availability for operational assignments.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": 'evelyn.wilson9461@example.com'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'V25KYO'}
            ),

            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'first', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'LGA'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": 'AC003', "start_date": '2024-05-21', "end_date": '2024-05-21'}
            )
        ],
        outputs={
            "customer_profile": "{'first_name': 'Chen', 'last_name': 'Hernandez'}'s gold tier member profile with membership benefits and account information",
            "reservation_details": "Current reservation V25KYO details showing the business class flight from EWR to LGA",
            "daily_schedule": "Complete flight schedule for 2024-05-21 showing all airline operations and available flights across the network",
            "reservation_update": "Reservation V25KYO update confirmation showing successful modification of cabin class, insurance, and baggage settings",
            "operational_events": "Operational events and disruptions for period from 2024-05-21 to 2024-05-21 showing 0 events",
            "airport_facilities": "LaGuardia Airport facilities and maintenance support infrastructure details for operational coordination",
            "captain_availability": "Current availability of 4 active Flight Attendant crew members for aircraft assignments and operational readiness",
            "maintenance_logs": "Maintenance logs for aircraft AC003 on May 21, 2024 showing maintenance activities, issues, and operational readiness status"
        }
    ),
    Task(
        annotator="0",
        user_id="user_32",
        instruction="You are a comprehensive crew operations manager responsible for optimizing crew scheduling, operational readiness, and airport facility coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-16, end date 2024-05-21, airport ORD. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and coordinate with airport facilities for seamless operations. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, operational monitoring, and airport facility information. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, review operational events within the specified window, and obtain airport facility information for ORD to support operational coordination.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-16', "end_date": '2024-05-21'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015'",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020'",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain' and status 'Active'",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant' and status 'Active'",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew action with crew_id 'CM015' and role 'Captain'",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status action with aircraft_id 'AC003' and new_status 'Maintenance'",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320' and expiry_threshold_days 30",
            "operational_events": "Operational events and disruptions for period from 2024-05-16 to 2024-05-21 showing coordination requirements retrieved via get_operational_events with start_date '2024-05-16' and end_date '2024-05-21'",
            "airport_facilities": "Airport facility information for ORD airport retrieved via get_airport_details_by_iata_code with iata_code 'ORD' showing terminal facilities, ground support equipment, and operational infrastructure for comprehensive airport coordination and operational planning"
        }
    ),

    Task(
        annotator="0",
        user_id="user_33",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, and update aircraft AC003 status to Maintenance.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            )
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance"
        }
    ),
    Task(
        annotator="0",
        user_id="user_34",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-16, end date 2024-05-21. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review operational events within the specified window.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-16', "end_date": '2024-05-21'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-16 to 2024-05-21 showing coordination requirements"
        }
    ),
    Task(
        annotator="0",
        user_id="user_35",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC004, certification type A320, expiry threshold days 30, role Captain, status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status. The objective is to activate crew members CM015 and CM020 for operational assignments, update CM015's role to Captain, schedule maintenance for aircraft AC004, and verify A320 certification status.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions with crew_member_id 'CM015' and 'CM020', new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC004 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC004', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320', expiry_threshold_days 30 for certification monitoring"
        }
    ),
    Task(
        annotator="0",
        user_id="user_36",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-10, end date 2024-05-12. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review operational events within the specified window.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-10', "end_date": '2024-05-12'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-10 to 2024-05-12 showing coordination requirements"
        }
    ),
    Task(
        annotator="0",
        user_id="user_37",
        instruction=(
            "You are 'crew.manager@airlineops.com'. The operations team needs to optimize crew scheduling and operational readiness for the upcoming flight schedule. You need to finalize crew arrangements with the following details:\n"
            "- Crew member: CM015 (status: Active)"
            "- Crew member: CM020 (status: Active)"
            "- Role update: Update CM015's role to Captain"
            "- Availability check: Captain crew members (Active status)"
            "- Availability check: Flight Attendant crew members (Active status)"
            "- Certification verification: A320 aircraft type"
            "- Expiry threshold: 30 days for certification monitoring"
            "- Notes: Crew activation and certification verification completed for operational readiness."
        ),      
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 information retrieved and status confirmed",
            "crew_details_20": "Crew member CM020 information retrieved and status confirmed", 
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "crew_certifications": "A320 certification status verified with 30-day expiry threshold monitoring completed"
        }
    ),

    Task(
        annotator="0",
        user_id="user_38",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, role Flight Attendant, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through comprehensive maintenance coordination. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status management. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across Captain and Flight Attendant crew categories, update CM015's role to Captain, and schedule maintenance for aircraft AC003 to ensure operational readiness and maintenance coordination."
        ,
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for operational coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for operational planning",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew management",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive crew coordination",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for optimal crew placement",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance coordination"
        }
    ),

    Task(
        annotator="0",
        user_id="user_39",
        instruction="Manage crew operations responsible for optimizing crew scheduling, operational readiness, and comprehensive operational coordination. You need to work with: crew member CM013, crew member CM017, aircraft AC004, certification type B737, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through detailed aircraft and certification analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, and crew certification monitoring. The objective is to activate crew members CM013 and CM017 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM013 crew profile information, schedule maintenance for aircraft AC004, and verify B737 crew certification status for comprehensive operational management.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM013'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM017'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM013', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM017', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM013', "status": 'Active'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B737', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_13": "Crew member CM013 (Susan Martinez) - Captain based at BOS airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM013' for crew management coordination",
            "crew_details_17": "Crew member CM017 (Ashley Anderson) - Flight Attendant based at PHX airport, currently Active status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM017' for crew management coordination",
            "crew_updates": "Crew member CM013 status updated to Active, CM017 status updated to Active via update_crew_member_status actions for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_profile_update": "Crew member CM013 profile updated with Active status for operational readiness via update_crew_profile with crew_id 'CM013', status 'Active' for crew profile management",
            "aircraft_status": "Aircraft AC004 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC004', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for B737 aircraft showing certification details and expiry information retrieved via get_crew_certification_status with certification_type 'B737', expiry_threshold_days 30 for crew certification management"
        }
    ),
    Task(
        annotator="0",
        user_id="user_40",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring availability verification across all crew categories, update aircraft AC003 status to Maintenance, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),
    Task(
        annotator="0",
        user_id="user_41",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, and update CM015's role to Captain."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management"
        }
    ),

    Task(
        annotator="0",
        user_id="user_42",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            )
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),
    Task(
        annotator="0",
        user_id="user_43",
        instruction="Execute senior operations management responsible for customer service operations and comprehensive flight coordination. You need to work with: reservation V25KYO, destination LGA, date 2024-05-21, end date 2024-05-21, cabin class first, insurance yes, payment method credit_card_8453507, total baggages 3, nonfree baggages 1, airport LGA, role Flight Attendant, status Active, start date 2024-05-21, iata code LGA, flight operations and schedule optimization, aircraft model B737-800. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, and enhance operational coordination through comprehensive aircraft model analysis. You have access to manage: flight status monitoring, schedule management, operational events monitoring, airport facilities, crew availability, and aircraft model coordination.",
        actions=[
            Action(
                name="UpdateReservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'first', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'LGA'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={"model_id": 'B737-800'}
            ),
        ],
        outputs={
            "reservation_update": "Reservation V25KYO update confirmation showing successful modification of cabin class, insurance, and baggage settings via update_reservation with reservation_id 'V25KYO', cabin 'first', insurance 'yes', total_baggages 3, nonfree_baggages 1, payment_method_id 'credit_card_8453507' for reservation management",
            "reservation_details": "Detailed reservation information for V25KYO retrieved via get_reservation_details with reservation_id 'V25KYO' for customer service coordination",
            "operational_events": "Operational events and disruptions for period from 2024-05-21 to 2024-05-21 showing 0 events retrieved via get_operational_events with start_date '2024-05-21', end_date '2024-05-21' for operational monitoring",
            "airport_facilities": "LaGuardia Airport facilities and maintenance support infrastructure details for operational coordination retrieved via get_airport_details_by_iata_code with iata_code 'LGA' for airport facilities management",
            "flight_attendant_availability": "Current availability of 4 active Flight Attendant crew members for aircraft assignments and operational readiness retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for crew availability monitoring",
            "aircraft_model_info": "Aircraft B737-800 model specifications retrieved via get_aircraft_model_info with model_id 'B737-800' for comprehensive operational planning and aircraft coordination"
        }
    ),

    Task(
        annotator="0",
        user_id="user_44",
        instruction="You are a operations manager responsible for customer service operations. For gold customer daiki.johnson3136@example.com and reservation R9QDGB (LAX to BOS on 2024-05-28, flight HAT034), you need to process the customer's upgrade request by reviewing current reservation details and updating the reservation to first class with travel insurance and enhanced baggage allowance (5 total bags, 2 non-free). Ensure all changes comply with gold tier member benefits and company policies.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": 'daiki.johnson3136@example.com'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": 'LAX', "destination": 'BOS', "date": '2024-05-28'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={"flight_number": 'HAT034', "date": '2024-05-28'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={"reservation_id": 'R9QDGB', "cabin": 'first', "insurance": 'yes', "total_baggages": 5, "nonfree_baggages": 2, "payment_method_id": 'credit_card_6082923'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
        ],
        outputs={
            "customer_profile": "Gold tier member profile for Jennifer Johnson with account information and membership benefits",
            "reservation_details": "Current reservation R9QDGB showing economy class flight from LAX to BOS on 2024-05-28",
            "flight_availability": "Available flights from LAX to BOS on 2024-05-28 confirming route viability",
            "flight_status": "Flight HAT034 status for May 28, 2024 showing operational readiness",
            "reservation_update": "Reservation R9QDGB successfully updated to first class with insurance and 5 total bags",
            "updated_reservation": "Final reservation details showing upgraded cabin class, insurance, and enhanced baggage allowance",
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_45",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through effective aircraft maintenance coordination. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status updates. The objective is to first retrieve crew member information for CM015 and CM020, then activate both crew members to Active status, verify crew availability for Captain and Flight Attendant roles, update CM015's role to Captain, and finally update aircraft AC003 status to Maintenance for operational readiness and maintenance coordination.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for operational coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for operational planning",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew management",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive crew coordination",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for optimal crew placement",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance coordination"
        }
    ),

    Task(
        annotator="0",
        user_id="user_46",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC004, certification type B787-9, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC004, and verify B787-9 certification status.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC004 status updated to Maintenance",
            "crew_certifications": "Crew certification status for B787-9 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),

    Task(
        annotator="0",
        user_id="user_47",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, crew member CM023, status Active, role Captain, role Flight Attendant. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through focused availability verification. You have access to manage: crew status updates, crew role assignments, and crew availability monitoring. The objective is to activate crew members CM015, CM020, and CM023 for operational assignments while ensuring targeted availability verification across Captain and Flight Attendant crew categories, and update CM015's role to Captain for optimal crew placement."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM023', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for operational coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for operational planning",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active, CM023 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020', 'CM023' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew management",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive crew coordination",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for optimal crew placement"
        }
    ),

    Task(
        annotator="0",
        user_id="user_48",
        instruction=(
            "You are a crew management coordinator responsible for optimizing crew scheduling and operational readiness. You need to manage the following crew management tasks:\n"
            "- Crew Member: CM015 (status update to Active)\n"
            "- Crew Member: CM020 (status update to Active)\n"
            "- Crew Role: Captain (assignment for CM015)\n"
            "- Aircraft: AC003 (Maintenance status)\n"
            "- Certification: A320 (30-day expiry threshold)\n"
            "- Availability Check: Captain (Active status)\n"
            "- Availability Check: Flight Attendant (Active status)\n"
            "- Operational Period: 2024-05-21 to 2024-05-23\n"
            "- Notes: Crew management coordination completed with status updates, role assignments, aircraft maintenance scheduling, certification monitoring, and operational event tracking"
        ),       
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),  
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-23'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-21 to 2024-05-23 showing coordination requirements"
        }
    ),

    Task(
        annotator="0",
        user_id="user_49",
        instruction="Execute senior crew operations management responsible for comprehensive crew deployment, certification oversight, aircraft coordination, and crew availability management. You need to work with: crew member CM015 (Olivia Johnson), crew member CM020 (Mohamed Lopez), B787-9 aircraft model, and comprehensive crew availability monitoring. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, enhance operational coordination through aircraft model analysis, and ensure comprehensive crew availability across all roles. You have access to manage: crew information gathering, status management, role optimization, certification compliance monitoring, aircraft model coordination, and crew availability assessment. The objective is to optimize crew deployment by ensuring CM015 and CM020 are properly activated, assign Captain role specifically to CM015, check existing certification compliance for B787-9 aircraft operations without modifying certifications, assess aircraft model specifications for operational planning, and ensure comprehensive crew availability across all required roles for operational readiness.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={"model_id": 'B787-9'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
        ],
        outputs=[
            "crew_info_retrieved:CM015",
            "crew_info_retrieved:CM020",
            "crew_status_updated:CM015:Active",
            "crew_status_updated:CM020:Active",
            "crew_availability_checked:Captain:Active",
            "crew_role_updated:CM015:Captain",
            "crew_certification_verified:B787-9:30_days",
            "aircraft_model_info:B787-9",
            "crew_availability_checked:Flight_Attendant:Active"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_50",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring availability verification, update aircraft AC003 status to Maintenance, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),

    Task(
        annotator="0",
        user_id="user_51",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring availability verification across all crew categories, update CM015's role to Captain, and schedule maintenance for aircraft AC003."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance scheduling"
        }
    ),
    Task(
        annotator="0",
        user_id="user_52",
        instruction=(
            "You are a crew management coordinator responsible for optimizing crew scheduling and operational readiness. You need to manage the following crew management tasks:\n"
            "- Crew Member: CM015 (status update to Active)\n"
            "- Crew Member: CM020 (status update to Active)\n"
            "- Crew Role: Captain (assignment for CM015)\n"
            "- Aircraft: AC003 (Maintenance status)\n"
            "- Certification: A320 (30-day expiry threshold)\n"
            "- Availability Check: Captain (Active status)\n"
            "- Availability Check: Flight Attendant (Active status)\n"
            "- Operational Period: 2024-03-25 to 2024-03-31\n"
            "- Maintenance Type: A-Check\n"
            "- Notes: Crew management coordination completed with status updates, role assignments, and operational monitoring"
        ),       
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),  
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-03-25', "end_date": '2024-03-31'}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"start_date": '2024-03-25', "end_date": '2024-03-31', "maintenance_type": 'A-Check'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-03-25 to 2024-03-31 showing coordination requirements",
            "maintenance_records": "Aircraft maintenance records for specified period showing scheduled maintenance logs with maintenance type 'A-Check'"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_53",
        instruction="Execute senior operations management responsible for customer service operations and crew coordination. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, flight HAT165, date 2024-05-27, airport ORD, start date 2024-05-27, end date 2024-05-27, crew member CM001, operational events for 2024-05-27, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, enhance operational coordination through crew member integration, and maintain operational awareness through comprehensive event monitoring. You have access to manage: flight status monitoring, schedule management, crew member coordination, and operational event monitoring. The objective is to retrieve customer profile for Olivia Santos, review reservation KDBNYP details, process reservation cancellation, monitor flight HAT165 status for operational coordination, evaluate ORD airport facilities, review daily flight schedule for strategic planning, coordinate with crew member CM001 for enhanced operational readiness and crew management integration, and monitor operational events for 2024-05-27 to ensure comprehensive operational awareness and proactive disruption management.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="CancelReservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),

            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
        ],
        outputs={
            "customer_profile": "Olivia Santos's gold tier member profile retrieved via get_user_profile with user_email 'sophia.santos7908@example.com' showing membership benefits and account information for customer service coordination",
            "reservation_details": "Current reservation KDBNYP details retrieved via get_reservation_details with reservation_id 'KDBNYP' showing business class flight from ORD to EWR for strategic reservation management",
            "cancellation_result": "Reservation KDBNYP cancellation confirmation showing successful cancellation status and refund processing details via cancel_reservation with reservation_id 'KDBNYP' for customer service resolution",
            "flight_status": "Flight HAT165 status for May 27, 2024 from ORD to IAH retrieved via get_flight_status_by_number_and_date with flight_number 'HAT165', date '2024-05-27' showing operational status for flight operations monitoring",
            "airport_facilities": "O'Hare International Airport facilities and maintenance support infrastructure details retrieved via get_airport_details_by_iata_code with iata_code 'ORD' for operational coordination and infrastructure assessment",
            "daily_schedule": "Complete flight schedule for 2024-05-27 showing all airline operations and available flights across the network retrieved via get_flight_schedule with start_date '2024-05-27', end_date '2024-05-27' for strategic scheduling optimization",
            "crew_member_details": "Crew member CM001 (Isabella Brown) - Captain based at ATL airport, currently Active status, with flight experience on B737-800 aircraft retrieved via get_crew_member_info with crew_id 'CM001' for enhanced operational coordination and crew management integration",
            "operational_events": "Operational events for May 27, 2024 retrieved via get_operational_events with start_date '2024-05-27', end_date '2024-05-27' showing potential disruptions, gate changes, and operational incidents for comprehensive operational awareness and proactive disruption management"
        }
    ),
     
    Task(
        annotator="0",
        user_id="user_54",
        instruction="Execute senior operations management responsible for customer service operations and comprehensive crew coordination. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, flight HAT165, date 2024-05-27, airport ORD, start date 2024-05-27, end date 2024-05-27, crew member CM001, crew member CM003, crew member CM004. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, enhance operational coordination through comprehensive crew member integration. You have access to manage: flight status monitoring, schedule management, crew member coordination. The objective is to retrieve customer profile for Olivia Santos, review reservation KDBNYP details, process reservation cancellation, monitor flight HAT165 status for operational coordination, evaluate ORD airport facilities, review daily flight schedule for strategic planning, coordinate with crew member CM001 for enhanced operational readiness, integrate crew member CM003 (Mohamed Lopez) for flight attendant coordination, and incorporate crew member CM004 (Jennifer Wilson) for captain management."
        ,actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="CancelReservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),

            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": "CM003"}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": "CM004"}
            ),
        ],
        outputs={
            "customer_profile": "Olivia Santos's gold tier member profile retrieved via get_user_profile with user_email 'sophia.santos7908@example.com' showing membership benefits and account information for customer service coordination",
            "reservation_details": "Current reservation KDBNYP details retrieved via get_reservation_details with reservation_id 'KDBNYP' showing business class flight from ORD to EWR for strategic reservation management",
            "cancellation_result": "Reservation KDBNYP cancellation confirmation showing successful cancellation status and refund processing details via cancel_reservation with reservation_id 'KDBNYP' for customer service resolution",
            "flight_status": "Flight HAT165 status for May 27, 2024 from ORD to IAH retrieved via get_flight_status_by_number_and_date with flight_number 'HAT165', date '2024-05-27' showing operational status for flight operations monitoring",
            "airport_facilities": "O'Hare International Airport facilities and maintenance support infrastructure details retrieved via get_airport_details_by_iata_code with iata_code 'ORD' for operational coordination and infrastructure assessment",
            "daily_schedule": "Complete flight schedule for 2024-05-27 showing all airline operations and available flights across the network retrieved via get_flight_schedule with start_date '2024-05-27', end_date '2024-05-27' for strategic scheduling optimization",
            "crew_member_details_cm001": "Crew member CM001 (Isabella Brown) - Captain based at ATL airport, currently Active status, with flight experience on B737-800 aircraft retrieved via get_crew_member_info with crew_id 'CM001' for enhanced operational coordination and crew management integration",
            "crew_member_details_cm003": "Crew member CM003 (Mohamed Lopez) - Flight Attendant based at ORD airport, currently Active status, with flight experience on A320neo aircraft retrieved via get_crew_member_info with crew_id 'CM003' for flight attendant coordination and passenger service management",
            "crew_member_details_cm004": "Crew member CM004 (Jennifer Wilson) - Captain based at LAX airport, currently Active status, with flight experience on B787-9 aircraft retrieved via get_crew_member_info with crew_id 'CM004' for captain management and flight operations leadership"
        }
    ),

    Task(
        annotator="0",
        user_id="user_55",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with crew member CM015 and crew member CM020, aircraft AC003, role Captain, status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through aircraft coordination. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status updates. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification for Captain roles, update CM015's role to Captain, and schedule maintenance for aircraft AC003.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions with crew_member_id 'CM015' and 'CM020', new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for operational readiness and maintenance scheduling"
        }
    ),

    Task(
        annotator="0",
        user_id="user_56",
        instruction="Manage crew operations responsible for optimizing crew scheduling, operational readiness, and comprehensive operational coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC004, certification type B787-9, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through detailed aircraft analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and aircraft model coordination. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC004, verify B787-9 certification status, and retrieve detailed A350-900 aircraft model specifications for comprehensive operational planning.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B787-9', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={"model_id": 'A350-900'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC004 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC004', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for B787-9 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'B787-9', expiry_threshold_days 30 for certification monitoring",
            "aircraft_model_info": "Aircraft A350-900 model specifications retrieved via get_aircraft_model_info with model_id 'A350-900' for comprehensive aircraft coordination and operational planning"
        }
    ),

    Task(
        annotator="0",
        user_id="user_57",
        instruction="Manage crew operations responsible for optimizing crew scheduling, operational readiness, and comprehensive aircraft coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC004, certification type B787-9, expiry threshold days 30, role Captain, status Active, new status Active, aircraft model B787-9, airport ATL. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through detailed aircraft analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, aircraft model coordination, and airport details coordination. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC004, verify B787-9 certification status, retrieve detailed B787-9 aircraft model specifications for operational planning, and obtain comprehensive airport details for ATL airport coordination.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B787', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetAircraftModelInfo",
                kwargs={"model_id": 'B787-9'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ATL'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC004 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC004', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for B787-9 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'B787-9', expiry_threshold_days 30 for certification monitoring",
            "aircraft_model_info": "Aircraft B787-9 model specifications retrieved via get_aircraft_model_info with model_id 'B787-9' for comprehensive aircraft coordination and operational planning",
            "airport_details": "ATL airport details retrieved via get_airport_details_by_iata_code with iata_code 'ATL' for comprehensive airport coordination and operational planning"
        }
    ),

    Task(
        annotator="0",
        user_id="user_58",
        instruction="Manage crew operations responsible for optimizing crew scheduling, operational readiness, and comprehensive operational coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC004, certification type B787-9, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through detailed maintenance analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and maintenance logs coordination. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC004, verify B787-9 certification status, and retrieve detailed maintenance logs for AC004 aircraft operational planning.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC004', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B787', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": 'AC004'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC004 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC004', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for B787-9 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'B787-9', expiry_threshold_days 30 for certification monitoring",
            "maintenance_logs": "Maintenance logs for aircraft AC004 retrieved via get_maintenance_logs with aircraft_id 'AC004' for comprehensive maintenance coordination and operational planning"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_59",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. For crew members CM004 and CM008, activate them for operational assignments and update CM004's role to Captain. Assess crew availability across all categories and verify B737 certification status. Make strategic crew management decisions to ensure operational efficiency and update CM004's home base to DFW for optimal crew deployment and operational coordination. Review crew member schedule to verify operational readiness and deployment effectiveness.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM004'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM004', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM008', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM004', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'B737'}
            ),
            Action(
                name="UpdateCrewMemberHomeBase",
                kwargs={"crew_id": 'CM004', "new_home_base": 'DFW'}
            ),
            Action(
                name="GetCrewMemberSchedule",
                kwargs={"crew_id": 'CM004'}
            ),
        ],
        outputs={
            "crew_details_4": "Crew member CM004 information and current status",
            "crew_details_8": "Crew member CM008 information and current status",
            "crew_updates": "Status updates for both crew members",
            "crew_availability_captains": "Current availability of active Captain crew members",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members",
            "crew_assignment": "CM004 role update confirmation",
            "crew_certifications": "B737 certification status for crew members",
            "home_base_update": "Crew member CM004 home base updated to DFW for operational efficiency",
            "crew_schedule": "CM004 crew member schedule showing operational assignments and deployment readiness"
        }
    ),

    Task(
        annotator="0",
        user_id="user_60",
        instruction="Execute senior crew operations management responsible for comprehensive crew management and airport facility coordination. You need to work with: crew member CM015 (Olivia Johnson) based at ORD airport, crew member CM020 (Mohamed Lopez) based at CLT airport, O'Hare International Airport (ORD), and Raleigh Douglas International Airport (CLT). Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through airport facility evaluation. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and airport facility assessment. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, and evaluate their home base airport facilities for operational readiness and crew base operations.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ORD'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'CLT'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "ord_airport_details": "O'Hare International Airport (ORD) facilities and operational details showing terminal information, services, and ground operations capabilities for crew base operations",
            "clt_airport_details": "Charlotte Douglas International Airport (CLT) facilities and operational details showing terminal information, services, and ground operations capabilities for crew base operations"
        }
    ),

    Task(
        annotator="0",
        user_id="user_61",
        instruction="Manage crew operations responsible for optimizing crew scheduling, operational readiness, and focused aircraft coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through targeted aircraft analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, and crew certification status. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, and verify A320 certification status for operational readiness."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320', expiry_threshold_days 30 for certification monitoring"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_62",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, and verify A320 certification status.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),
    Task(
        annotator="0",
        user_id="user_63",
        instruction=(
            "You are 'crew.manager@airlineops.com'. The operations team needs to optimize crew scheduling and operational readiness for the upcoming flight schedule. You need to finalize crew arrangements with the following details:\n"
            "- Crew member: CM015 (status: Active)\n"
            "- Crew member: CM020 (status: Active)\n"
            "- Role assignment: Captain for CM015\n"
            "- Availability check: Captain crew members (Active status)\n"
            "- Availability check: Flight Attendant crew members (Active status)\n"
            "- Certification verification: A320 aircraft type\n"
            "- Expiry threshold: 30 days for certification monitoring\n"
            "- Crew assignment retrieval: Current assignments for CM015\n"
            "- Notes: Crew activation, role assignment, availability verification, certification monitoring, and assignment retrieval completed for comprehensive operational readiness."
        ),      
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="ManageCrewMember",
                kwargs={"action": "get_assignments", "crew_id": 'CM015'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 information retrieved using get_crew_member_info tool with crew_id parameter",
            "crew_details_20": "Crew member CM020 information retrieved using get_crew_member_info tool with crew_id parameter", 
            "crew_updates": "Crew member CM015 status updated to Active using update_crew_member_status tool, CM020 status updated to Active using update_crew_member_status tool",
            "crew_availability_captains": "Current availability of active Captain crew members retrieved using get_crew_availability tool with role and status parameters",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members retrieved using get_crew_availability tool with role and status parameters",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain using update_crew tool with crew_id and role parameters",
            "crew_certifications": "A320 certification status verified using get_crew_certification_status tool with certification_type and expiry_threshold_days parameters",
            "crew_assignments": "Current crew assignments for CM015 retrieved using manage_crew_member tool with get_assignments action and crew_id parameter"
        }
    ),

    Task(
        annotator="0",
        user_id="user_64",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories."
        ,
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),  
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
        }
    ),

    Task(
        annotator="0",
        user_id="user_65",
        instruction="You are a customer service operations specialist responsible for comprehensive customer account management and service optimization. Your primary responsibility involves customer profile retrieval for sophia.santos7908@example.com, reservation details management for KDBNYP, reservation cancellation processing, alternative flight discovery from ORD to IAH on 2024-05-27, flight status monitoring for HAT165 on 2024-05-27, airport facility coordination for ORD, flight schedule management for 2024-05-27, and membership level enhancement from gold to platinum. The workflow integrates customer information gathering, reservation lifecycle management, flight availability discovery, flight operations monitoring, airport infrastructure coordination, schedule optimization, and membership tier enhancement for premium customer service delivery. Your coordination efforts should ensure seamless customer profile management, efficient reservation processing, effective alternative flight discovery, accurate flight status tracking, comprehensive airport facility coordination, optimal schedule management, and enhanced membership benefits for superior customer experience. Key parameters: customer_email=sophia.santos7908@example.com, reservation_id=KDBNYP, origin=ORD, destination=IAH, flight_date=2024-05-27, flight_number=HAT165, airport_code=ORD, schedule_date=2024-05-27, new_membership=platinum",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
             Action(
                name="CancelReservation",
                kwargs={
                    "reservation_id": "KDBNYP"
                }
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-27"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="UpdateUserMembership",
                kwargs={"user_email": "sophia.santos7908@example.com", "new_membership": "platinum"}
            )
        ],
        outputs=[
            "user_profile_retrieved:sophia.santos7908@example.com",
            "reservation_details_retrieved:KDBNYP",
            "reservation_cancelled:KDBNYP",
            "flights_found:ORD:IAH:2024-05-27",
            "flight_status_checked:HAT165:2024-05-27",
            "airport_details_retrieved:ORD",
            "flight_schedule_retrieved:2024-05-27",
            "membership_updated:sophia.santos7908@example.com:platinum"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_66",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring availability verification across all crew categories, update aircraft AC003 status to Maintenance, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),
    Task(
        annotator="0",
        user_id="user_67",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring availability verification across all crew categories.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
        }
    ),
    Task(
        annotator="0",
        user_id="user_68",
        instruction="Manage crew operations responsible for optimizing crew scheduling, operational readiness, and comprehensive aircraft coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through detailed aircraft analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and aircraft details coordination. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, verify A320 certification status, and retrieve comprehensive aircraft B787-9 model details for operational planning.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetAircraftByModel",
                kwargs={"model_id": 'B787-9'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320', expiry_threshold_days 30 for certification monitoring",
            "aircraft_details": "Aircraft B787-9 model details retrieved via get_aircraft_by_model with model_id 'B787-9' for comprehensive aircraft coordination and operational planning"
        }
    ),
    Task(
        annotator="0",
        user_id="user_69",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, and update aircraft AC003 status to Maintenance.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance"
        }
    ),
    Task(
        annotator="0",
        user_id="user_70",
        instruction="Manage crew operations responsible for optimizing crew scheduling, operational readiness, and comprehensive airport coordination. You need to work with: crew member CM015, crew member CM020, aircraft AC003, certification type A320, expiry threshold days 30, role Captain, status Active, new status Active, airport ORD. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational coordination through detailed airport facility analysis. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status updates, crew certification status, and airport facility coordination. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, schedule maintenance for aircraft AC003, verify A320 certification status, and retrieve comprehensive ORD airport details for operational planning and crew coordination.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance scheduling",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320', expiry_threshold_days 30 for certification monitoring",
            "airport_facilities": "Chicago O'Hare International Airport (ORD) facilities and operational details retrieved via get_airport_details_by_iata_code with iata_code 'ORD' for comprehensive airport coordination and operational planning"
        }
    ),
    Task(
        annotator="0",
        user_id="user_71",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. Your role involves managing passenger reservations, ensuring flight operational efficiency, and maintaining high standards of service delivery. You need to address a customer service scenario involving reservation modifications, flight availability assessment, and operational coordination. Your responsibilities include: managing customer profiles and reservation changes according to airline policies, evaluating flight options and availability for optimal routing, monitoring flight status and operational conditions, assessing operational events that may impact service quality, coordinating with airport facilities for smooth operations, and ensuring aircraft maintenance readiness for safe operations. You have access to tools for reservation management, customer service coordination, flight operations monitoring, and maintenance oversight.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "ATL", "date": "2024-05-27"}
            ),
            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "cabin": "business",
                    "insurance": "yes",
                    "total_baggages": 2,
                    "flights": [
                        {
                            "origin": "ORD",
                            "destination": "ATL",
                            "flight_number": "HAT093",
                            "date": "2024-05-27",
                            "price": 450
                        }
                    ]
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT093", "date": "2024-05-27"}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": "AC001", "start_date": "2024-05-01", "end_date": "2024-05-01"}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": "CM001"}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetAircraftByModel",
                kwargs={"model_id": "B737-800"}
            )
        ],
        outputs={
            "customer_profile": "Olivia Santos gold tier member profile with membership benefits",
            "reservation_details": "Current reservation KDBNYP details showing ORD to ATL flight in business class",
            "alternative_flights": "Available alternative flights from ORD to ATL on May 27, 2024 for rebooking options",
            "reservation_update": "Updated reservation with cabin class business, insurance yes, total_baggages: 2, and flight change to ORD-ATL route",
            "reservation_confirmation": "Confirmed reservation details after updates with cabin class, insurance, baggage changes, and corrected flight route",
            "flight_status": "Flight HAT093 status for May 27, 2024 showing operational details, origin/destination, scheduled times, and availability",
            "operational_events": "Operational events and disruptions for May 1, 2024 showing delays, weather impacts, and technical issues affecting flight operations",
            "airport_facilities": "Chicago O'Hare International Airport (ORD) facilities and operational details showing terminal information, services, and ground operations capabilities",
            "maintenance_logs": "Maintenance logs for aircraft AC001 on May 1, 2024 showing maintenance activities, issues, and operational readiness status",
            "crew_details": "Crew member CM001 details showing role, status, flight experience, and operational qualifications",
            "flight_schedule": "Flight schedule for May 27, 2024 showing all available flights, routes, and operational timing for comprehensive flight planning",
            "aircraft_by_model": "Aircraft by model B737-800 showing available aircraft, their configurations, and operational readiness for flight assignments"
        }
    ),

    Task(
        annotator="0",
        user_id="user_72",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, cabin class business, insurance yes, total baggages 2. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, maintain operational awareness through flight status monitoring, ensure operational excellence through event tracking, enhance operational coordination through airport facilities evaluation, and ensure operational readiness through maintenance tracking. You have access to manage: reservation lifecycle management, customer profile handling, flight search operations, flight status monitoring, operational event assessment, airport facilities coordination, and aircraft maintenance monitoring. The objective is to update reservation KDBNYP to business class with travel insurance and 2 total baggages, while preserving all existing flight details and itinerary information.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "ATL", "date": "2024-05-27"}
            ),
            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "cabin": "business",
                    "insurance": "yes",
                    "total_baggages": 2
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT093", "date": "2024-05-27"}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": "AC003", "start_date": "2024-05-27", "end_date": "2024-05-27"}
            )
        ],
        outputs={
            "customer_profile": "Customer profile information retrieved",
            "reservation_details": "Current reservation details retrieved",
            "alternative_flights": "Available alternative flights found",
            "reservation_update": "Reservation updated with requested changes",
            "reservation_confirmation": "Updated reservation details confirmed",
            "flight_status": "Flight status information retrieved",
            "operational_events": "Operational events and disruptions retrieved",
            "airport_facilities": "Airport facilities information retrieved",
            "maintenance_logs": "Aircraft maintenance logs retrieved"
        }
    ),

    Task(
        annotator="0",
        user_id="user_73",
        instruction="Execute senior operations management responsible for customer service operations. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, origin ORD, destination EWR, date 2024-05-27, cabin class business, insurance yes, total baggages 2, nonfree baggages 1, flight HAT165, flight operations management. Your goals are to: optimize customer experience through reservation management, ensure efficient flight operations. You have access to tools for managing flight status, schedule, cabin class, insurance, and baggage.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "EWR", "date": "2024-05-27"}
            ),
            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "cabin": "business",
                    "insurance": "yes",
                    "total_baggages": 2,
                    "nonfree_baggages": 1
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT165",
                    "date": "2024-05-27"
                }
            )
        ],
        outputs={
            "customer_profile": "Olivia Santos gold tier member profile with membership benefits and account information retrieved via get_user_profile with user_email 'sophia.santos7908@example.com' for customer service assessment",
            "reservation_details": "Current reservation KDBNYP details showing ORD to EWR flight in economy class retrieved via get_reservation_details with reservation_id 'KDBNYP' for reservation management",
            "alternative_flights": "Available alternative flights from ORD to EWR on May 27, 2024 retrieved via find_flights with origin 'ORD', destination 'EWR', date '2024-05-27' for rebooking options",
            "reservation_update": "Reservation KDBNYP successfully upgraded to business class with travel insurance and baggage allowance via update_reservation with reservation_id 'KDBNYP', cabin 'business', insurance 'yes', total_baggages 2, nonfree_baggages 1",
            "reservation_confirmation": "Confirmed reservation details after updates retrieved via get_reservation_details with reservation_id 'KDBNYP' showing business class cabin, insurance coverage, and baggage changes",
            "flight_status": "Flight HAT165 status for May 27, 2024 retrieved via get_flight_status_by_number_and_date with flight_number 'HAT165', date '2024-05-27' showing operational details and schedule information"
        }
    ),

    Task(
        annotator="0",
        user_id="user_74",
        instruction=(
            "You are 'crew.manager@airlineops.com'. Crew members CM025 need to be activated for operational assignments with role updates and home base modifications. You need to finalize their arrangements with the following details:\n"
            "- Crew member: CM025 (status update to Active)"
            "- Role assignment: CM025 promoted to Captain"
            "- Availability check: Active Captains for operational assignments"
            "- Home base update: CM025 assigned to LAX airport"
            "- Aircraft status update: AC001 to Active for operational readiness"
            "- Notes: Crew members activated, role assigned, home base updated, and aircraft status verified for operational readiness."
        ),
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM025'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM025', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM025', "role": 'Captain'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberHomeBase",
                kwargs={"crew_id": 'CM025', "new_home_base": 'LAX'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC001', "new_status": 'Active'}
            ),
        ],
        outputs={
            "crew_member_25_activation": "Crew member CM025 status successfully updated to Active for operational assignments",
            "role_assignment": "Crew member CM025 successfully promoted to Captain role for operational assignments",
            "captain_availability": "Active Captain crew availability verified for operational assignments",
            "home_base_assignment": "Crew member CM025 successfully assigned to LAX airport home base",
            "aircraft_status_update": "Aircraft AC001 status successfully updated to Active for operational readiness",
            "operational_readiness": "Crew members activated, role assigned, home base updated, and aircraft status verified for operational readiness"
        }
    ),

    Task(
        annotator="0",
        user_id="user_75",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, role Captain, status Active. Your goals are to: ensure optimal crew placement for operational efficiency and maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, and crew availability monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories and update CM015's role to Captain for strategic crew placement.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions with crew_member_id 'CM015' and 'CM020', new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management"
        }
    ),

    Task(
        annotator="0",
        user_id="user_76",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-15, end date 2024-05-20. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review operational events for coordination requirements.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-15 to 2024-05-20 showing coordination requirements"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_77",
        instruction="Execute senior operations management responsible for customer service operations. For gold tier customer daiki.johnson3136@example.com and reservation R9QDGB (LAX to BOS via SFO on 2024-05-28, flight HAT034), process the customer's baggage enhancement request by checking their profile, reviewing current reservation details, verifying flight availability, checking flight status, and updating the reservation with enhanced baggage allowance (4 total bags, 2 non-free) and no travel insurance. Ensure all changes comply with gold tier member benefits and company policies.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": 'daiki.johnson3136@example.com'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": 'LAX', "destination": 'SFO', "date": '2024-05-28'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={"flight_number": 'HAT034', "date": '2024-05-28'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={"reservation_id": 'R9QDGB', "insurance": 'no', "total_baggages": 4, "nonfree_baggages": 2, "payment_method_id": 'credit_card_6082923'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'R9QDGB'}
            ),
        ],
        outputs={
            "customer_profile": "Gold tier member profile for Jennifer Johnson retrieved for baggage enhancement processing",
            "reservation_details": "Current reservation R9QDGB showing economy class flight from LAX to BOS via SFO on 2024-05-28",
            "flight_availability": "Available flights from LAX to SFO on 2024-05-28 confirming first leg route viability",
            "flight_status": "Flight HAT034 status for May 28, 2024 showing LAX to SFO operational readiness",
            "reservation_update": "Reservation R9QDGB successfully updated with no insurance and 4 total bags (2 non-free)",
            "updated_reservation": "Final reservation details showing enhanced baggage allowance and no travel insurance",
        }
    ),

    Task(
        annotator="0",
        user_id="user_78",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to tools for managing crew status, role assignments, availability monitoring, aircraft status, and certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),

    Task(
        annotator="0",
        user_id="user_79",
        instruction="You are a crew deployment coordinator responsible for comprehensive crew management and operational readiness assessment. Your primary responsibility involves crew member information retrieval for CM008 and CM012, crew status activation for CM012, crew profile updates for role assignments (CM008 to Captain, CM012 to Flight Attendant), and comprehensive availability monitoring across both Captain and Flight Attendant roles. The workflow integrates crew information gathering, status management, profile optimization, and dual-role availability assessment for strategic crew deployment planning. Your coordination efforts should ensure seamless crew information retrieval, effective status activation, precise role assignments through profile updates, and thorough availability monitoring across critical crew categories for optimal airline operations management. Key parameters: crew_id_1=CM008, crew_id_2=CM012, new_status=Active, role_1=Captain, role_2=Flight_Attendant",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM012'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM012', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM008', "role": 'Captain'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM012', "role": 'Flight Attendant'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
        ],
        outputs=[
            "crew_member_info_retrieved:CM008",
            "crew_member_info_retrieved:CM012",
            "crew_status_updated:CM012:Active",
            "crew_profile_updated:CM008:Captain",
            "crew_profile_updated:CM012:Flight_Attendant",
            "crew_availability_checked:Flight_Attendant",
            "crew_availability_checked:Captain"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_80",
        instruction="You are a senior customer service operations manager responsible for comprehensive reservation management, flight operations coordination, and operational event monitoring. You need to work with: reservation NO6JO3, customer emma.smith8074@example.com, flight HAT083 on 2024-05-16, Sacramento International Airport (LAX), first class cabin with travel insurance, payment method credit_card_4421486, and operational events monitoring for LAX on 2024-05-16. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, maintain operational awareness through flight status monitoring, ensure operational excellence through event tracking, and enhance operational coordination through airport facilities evaluation. You have access to manage: reservation lifecycle management, customer profile handling, flight status monitoring, schedule optimization, airport infrastructure assessment, and operational event monitoring. The objective is to retrieve reservation details for NO6JO3, manage customer profile for emma.smith8074@example.com, upgrade reservation to first class with insurance, verify post-upgrade reservation details, monitor HAT083 flight status on 2024-05-16, retrieve daily flight schedule for 2024-05-16, evaluate LAX airport facilities, and monitor operational events at LAX for comprehensive operational awareness and superior customer experience.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetUserProfile",
                kwargs={'user_email': 'emma.smith8074@example.com'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={'iata_code': 'LAX'}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16', 'airport_code': 'LAX'}
            ),
        ],
        outputs=[
            "reservation_details_retrieved:NO6JO3",
            "user_profile_retrieved:emma.smith8074@example.com",
            "reservation_updated:NO6JO3:first_class",
            "reservation_details_verified:NO6JO3",
            "flight_status_checked:HAT083:2024-05-16",
            "flight_schedule_retrieved:2024-05-16",
            "airport_details_retrieved:LAX",
            "operational_events_retrieved:LAX:2024-05-16"
        ]
    ),
    
    Task(
        annotator="0",
        user_id="user_81",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. You need to work with: customer sophia.santos7908@example.com, reservation KDBNYP, origin ORD, destination EWR via IAH, date 2024-05-27, cabin class business, insurance yes, total baggages 2, flight HAT165, airport ORD, aircraft AC003. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling, maintain operational awareness through flight status monitoring, ensure operational excellence through event tracking, enhance operational coordination through airport facilities evaluation, and ensure operational readiness through maintenance tracking. You have access to manage: reservation lifecycle management, customer profile handling, flight search operations, flight status monitoring, operational event assessment, airport facilities coordination, and aircraft maintenance monitoring.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "sophia.santos7908@example.com"}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": "ORD", "destination": "IAH", "date": "2024-05-27"}
            ),
            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "KDBNYP",
                    "cabin": "business",
                    "insurance": "yes",
                    "total_baggages": 2
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "KDBNYP"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT165", "date": "2024-05-27"}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": "2024-05-27", "end_date": "2024-05-27"}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "ORD"}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": "AC003", "start_date": "2024-05-27", "end_date": "2024-05-27"}
            )
        ],
        outputs={
            "customer_profile": "Olivia Santos gold tier member profile with membership benefits retrieved for service assessment",
            "reservation_details": "Current reservation KDBNYP details showing ORD to EWR via IAH routing in business class",
            "alternative_flights": "Available alternative flights from ORD to IAH on May 27, 2024 for rebooking options and route flexibility",
            "reservation_update": "Updated reservation with cabin class business, insurance yes, total_baggages: 2 according to customer requirements",
            "reservation_confirmation": "Confirmed reservation details after updates showing business class cabin, insurance coverage, and baggage allowance",
            "flight_status": "Flight HAT165 status for May 27, 2024 showing operational details, ORD to IAH route, scheduled times, and availability",
            "operational_events": "Operational events and disruptions for May 27, 2024 showing delays, weather impacts, and technical issues affecting flight operations",
            "airport_facilities": "Chicago O'Hare International Airport (ORD) facilities and operational details showing terminal information, services, and ground operations capabilities",
            "maintenance_logs": "Maintenance logs for aircraft AC003 on May 27, 2024 showing maintenance activities, issues, and operational readiness status"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_82",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-15, end date 2024-05-20. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review operational events for coordination requirements.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-15 to 2024-05-20 showing coordination requirements"
        }
    ),
    Task(
        annotator="0",
        user_id="user_83",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM008, crew member CM012, role Captain, role Flight Attendant, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through comprehensive availability verification. You have access to manage: crew status updates, crew role assignments, and crew availability monitoring. The objective is to activate crew members CM008 and CM012 for operational assignments, update CM008's role to Captain and CM012's role to Flight Attendant, and ensure comprehensive availability verification across Captain and Flight Attendant crew categories for operational readiness and strategic crew coordination."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM012'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM008', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM012', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM008', "role": 'Captain'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM012', "role": 'Flight Attendant'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
        ],
        outputs={
            "crew_details_8": "Crew member CM008 (Olivia Johnson) - First Officer based at LAS airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM008' for operational coordination",
            "crew_details_12": "Crew member CM012 (Elizabeth Brown) - First Officer based at MCO airport, currently Inactive status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM012' for operational planning",
            "crew_status_updates": "Crew member CM008 status updated to Active, CM012 status updated to Active via update_crew_member_status with crew_member_id 'CM008', 'CM012' and new_status 'Active' for operational readiness",
            "crew_role_updates": "Crew member CM008 role updated to Captain, CM012 role updated to Flight Attendant via update_crew_profile with crew_id 'CM008', role 'Captain' and crew_id 'CM012', role 'Flight Attendant' for optimal crew placement",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew management",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive crew coordination"
        }
    ),
    Task(
        annotator="0",
        user_id="user_84",
        instruction="Execute senior operations management responsible for comprehensive flight operations and customer service management. You need to work with: customer evelyn.wilson9461@example.com, reservation V25KYO, origin EWR, destination LGA, date 2024-05-21, end date 2024-05-21, cabin class business, insurance yes, payment method credit_card_8453507, total baggages 3, nonfree baggages 1, airport LGA, role Flight Attendant, status Active, aircraft AC003, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling while maintaining operational excellence, and ensure operational readiness through maintenance tracking. Focus on providing comprehensive operational oversight and customer service excellence across reservation lifecycle management, customer profile handling, flight search operations, schedule management, operational event monitoring, airport facilities evaluation, crew coordination, and aircraft maintenance monitoring.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": 'evelyn.wilson9461@example.com'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": 'EWR', "destination": 'LGA', "date": '2024-05-21'}
            ),

            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'business', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'LGA'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"aircraft_id": 'AC003', "start_date": '2024-05-21', "end_date": '2024-05-21'}
            )
        ],
        outputs={
            "customer_profile": "{'first_name': 'Chen', 'last_name': 'Hernandez'}'s gold tier member profile with membership benefits and account information",
            "reservation_details": "Current reservation V25KYO details showing the business class flight from EWR to LGA",
            "flight_schedule": "Flight schedule for 2024-05-21 showing 0 available flights from EWR to LGA",
            "daily_schedule": "Complete flight schedule for 2024-05-21 showing all airline operations and available flights across the network",
            "reservation_update": "Reservation V25KYO update confirmation showing successful modification of cabin class, insurance, and baggage settings",
            "operational_events": "Operational events and disruptions for period from 2024-05-21 to 2024-05-21 showing 0 events",
            "airport_facilities": "LaGuardia Airport facilities and maintenance support infrastructure details for operational coordination",
            "captain_availability": "Current availability of 4 active Flight Attendant crew members for aircraft assignments and operational readiness",
            "maintenance_logs": "Maintenance logs for aircraft AC003 on May 21, 2024 showing maintenance activities, issues, and operational readiness status"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_85",
        instruction="Execute senior crew operations management responsible for comprehensive crew management, certification compliance, and role optimization. You need to work with: crew member CM015 (Olivia Johnson), crew member CM020 (Mohamed Lopez), and A320 aircraft certification compliance. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, ensure regulatory compliance through certification monitoring, and optimize crew role assignments for operational readiness. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and crew certification compliance. The objective is to optimize crew deployment by ensuring CM015 and CM020 are properly activated and assigned to appropriate roles, verify comprehensive availability across all crew categories, ensure A320 certification compliance with 30-day expiry threshold, and achieve complete operational readiness for crew assignments.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM020', "role": 'Flight Attendant'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_certifications": "Crew certification status for A320 aircraft showing crew members with certifications expiring within 30 days",
            "crew_role_update": "Crew member CM020 role successfully updated to Flight Attendant for operational assignments"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_86",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with crew members CM015 and CM020. Your responsibility is to activate crew member CM015 for operational assignments and update their role to Captain, activate crew member CM020 for operational assignments, and ensure proper aircraft maintenance scheduling and crew certification compliance. Additionally, you need to coordinate aircraft maintenance activities to minimize operational disruption, monitor crew certification status to ensure regulatory compliance, and review operational events to identify any potential scheduling conflicts or resource constraints. All actions need align with company policies for crew management, operational safety, and regulatory compliance.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_87",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-14, end date 2024-05-19, maintenance type A-Check. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, operational monitoring, maintenance review. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review both operational events and maintenance logs within the specified window.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-14', "end_date": '2024-05-19'}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"start_date": '2024-05-14', "end_date": '2024-05-19', "maintenance_type": 'A-Check'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-14 to 2024-05-19 showing coordination requirements",
            "maintenance_records": "Aircraft maintenance records for specified period showing scheduled maintenance logs with maintenance type 'A-Check'"
        }
    ),

    Task(
        annotator="0",
        user_id="user_88",
        instruction="You are a crew deployment specialist responsible for comprehensive crew management and operational coordination. Your primary responsibility involves crew member information retrieval for CM015 and CM020, crew status activation for both crew members, comprehensive availability monitoring across Captain and Flight Attendant roles, crew role assignment for CM015 to Captain, aircraft status management for AC003 to Maintenance, crew certification verification for A320 aircraft with 30-day expiry threshold, maintenance log review for A-Check type from 2024-05-15 to 2024-05-20, and ORD airport facility coordination. The workflow integrates crew information gathering, status management, availability assessment, role assignment, aircraft maintenance coordination, certification monitoring, maintenance record analysis, and airport infrastructure assessment for comprehensive airline operations management. Your coordination efforts should ensure seamless crew activation, effective role assignments, thorough availability verification, proper aircraft maintenance scheduling, certification compliance, maintenance record review, and airport facility coordination for optimal operational efficiency. Key parameters: crew_id_1=CM015, crew_id_2=CM020, aircraft_id=AC003, new_status=Maintenance, certification_type=A320, expiry_threshold=30, maintenance_type=A-Check, airport_code=ORD, date_range=2024-05-15_to_2024-05-20",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20', "maintenance_type": 'A-Check'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ORD'}
            )
        ],
        outputs=[
            "crew_member_info_retrieved:CM015",
            "crew_member_info_retrieved:CM020",
            "crew_status_updated:CM015:Active",
            "crew_status_updated:CM020:Active",
            "crew_availability_checked:Captain",
            "crew_availability_checked:Flight_Attendant",
            "crew_role_updated:CM015:Captain",
            "aircraft_status_updated:AC003:Maintenance",
            "crew_certification_checked:A320",
            "maintenance_logs_retrieved:A-Check:2024-05-15_to_2024-05-20",
            "airport_details_retrieved:ORD"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_89",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, airport ORD. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, airport infrastructure. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review ORD airport facilities for operational coordination.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'ORD'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew members CM015 and CM020 statuses all updated to Active for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "ord_airport_facilities": "O'Hare International Airport facilities and maintenance support infrastructure details for operational coordination"
        }
    ),
    Task(
        annotator="0",
        user_id="user_90",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-15, end date 2024-05-20. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring, operational monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review operational events for coordination requirements.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetOperationalEvents",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "operational_events": "Operational events and disruptions for period from 2024-05-15 to 2024-05-20 showing coordination requirements"
        }
    ),

    Task(
        annotator="0",
        user_id="user_91",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments, verify crew availability for key operational roles, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015'",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020'",
            "crew_updates": "Crew members CM015 and CM020 statuses all updated to Active for operational readiness via update_crew_member_status actions",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain' and status 'Active'",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant' and status 'Active'",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew action with crew_id 'CM015' and role 'Captain'",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days retrieved via get_crew_certification_status with certification_type 'A320' and expiry_threshold_days 30"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_92",
        instruction="Execute senior operations management responsible for customer service operations. You need to work with: reservation V25KYO, origin EWR, destination LGA, date 2024-05-21, end date 2024-05-21, cabin class first, insurance yes, payment method credit_card_8453507, total baggages 3, nonfree baggages 1, airport LGA, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling.  You have access to manage: flight status monitoring, schedule management. ",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="FindFlights",
                kwargs={"origin": 'EWR', "destination": 'LGA', "date": '2024-05-21'}
            ),

            Action(
                name="GetFlightSchedule",
                kwargs={"start_date": '2024-05-21', "end_date": '2024-05-21'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={"reservation_id": 'V25KYO', "cabin": 'first', "insurance": 'yes', "total_baggages": 3, "nonfree_baggages": 1, "payment_method_id": 'credit_card_8453507'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": 'V25KYO'}
            ),
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": 'LGA'}
            ),
        ],
        outputs={
            "reservation_details": "Current reservation V25KYO details showing the business class flight from EWR to LGA",
            "flight_schedule": "Flight schedule for 2024-05-21 showing 0 available flights from EWR to LGA",
            "daily_schedule": "Complete flight schedule for 2024-05-21 showing all airline operations and available flights across the network",
            "reservation_update": "Reservation V25KYO update confirmation showing successful modification of cabin class, insurance, and baggage settings",
            "airport_facilities": "LaGuardia Airport facilities and maintenance support infrastructure details for operational coordination",
        }
    ),

    Task(
        annotator="0",
        user_id="user_93",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management, crew certification monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update aircraft AC003 status to Maintenance, and check crew certification status for A320 aircraft with expiry threshold of 30 days.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days"
        }
    ),

        Task(
        annotator="0",
        user_id="user_94",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, role Captain, status Active, new status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status management. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, and schedule maintenance for aircraft AC003."
        ,actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status with crew_member_id 'CM015', 'CM020' and new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for maintenance scheduling",
        }
    ),

    Task(
        annotator="0",
        user_id="user_95",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, aircraft status management. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories and update aircraft AC003 status to Maintenance.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015'",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020'",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain' and status 'Active'",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant' and status 'Active'",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew action with crew_id 'CM015' and role 'Captain'",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status action with aircraft_id 'AC003' and new_status 'Maintenance'"
        }
    ),
    
    Task(
        annotator="0",
        user_id="user_96",
        instruction="Manage crew operations responsible for updating crew member information and monitoring crew availability. You need to work with: crew member CM008, crew member CM012, role Captain, role Flight Attendant, status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew information retrieval, crew status updates, crew role assignments, crew availability monitoring. The objective is to retrieve crew member information for CM008 and CM012, update CM012 status to Active, assign CM008 to Captain role, assign CM012 to Flight Attendant role, and verify availability for both Captain and Flight Attendant roles.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM008'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM012'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM012', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM008', "role": 'Captain'}
            ),
            Action(
                name="UpdateCrewProfile",
                kwargs={"crew_id": 'CM012', "role": 'Flight Attendant'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
        ],
        outputs={
            "crew_details_8": "Crew member CM008 (Olivia Johnson) - First Officer based at LAS airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM008' for crew management coordination",
            "crew_details_12": "Crew member CM012 (Elizabeth Brown) - First Officer based at MCO airport, currently Inactive status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM012' for crew management coordination",
            "crew_status_update": "Crew member CM012 status updated to Active via update_crew_member_status with crew_member_id 'CM012', new_status 'Active' for operational readiness",
            "crew_role_updates": "Crew member CM008 role updated to Captain, CM012 role updated to Flight Attendant via update_crew_profile actions with crew_id 'CM008', role 'Captain' and crew_id 'CM012', role 'Flight Attendant' for strategic crew management",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for comprehensive availability verification"
        }
    ),

    Task(
        annotator="0",
        user_id="user_97",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, role Captain, status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management, and enhance operational readiness through aircraft coordination. You have access to manage: crew status updates, crew role assignments, crew availability monitoring, and aircraft status updates. The objective is to activate crew members CM015 and CM020 for operational assignments while ensuring comprehensive availability verification across all crew categories, update CM015's role to Captain, and schedule maintenance for aircraft AC003 to ensure operational readiness.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Flight Attendant', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions with crew_member_id 'CM015' and 'CM020', new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_availability_flight_attendants": "Current availability of active Flight Attendant crew members for operational assignments retrieved via get_crew_availability with role 'Flight Attendant', status 'Active' for comprehensive availability verification",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance via update_aircraft_status with aircraft_id 'AC003', new_status 'Maintenance' for operational readiness and maintenance scheduling"
        }
    ),

    Task(
        annotator="0",
        user_id="user_98",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015, crew member CM020, aircraft AC003, aircraft status Maintenance, certification type A320, expiry threshold days 30, start date 2024-05-15, end date 2024-05-20, maintenance type A-Check. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, aircraft status management, crew certification monitoring, maintenance scheduling. The objective is to activate crew members CM015 and CM020 for operational assignments, update CM015's role to Captain, update aircraft AC003 status to Maintenance, check crew certification status for A320 aircraft with expiry threshold of 30 days, and review maintenance logs for A-Check type from 2024-05-15 to 2024-05-20.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": 'AC003', "new_status": 'Maintenance'}
            ),
            Action(
                name="GetCrewCertificationStatus",
                kwargs={"certification_type": 'A320', "expiry_threshold_days": 30}
            ),
            Action(
                name="GetMaintenanceLogs",
                kwargs={"start_date": '2024-05-15', "end_date": '2024-05-20', "maintenance_type": 'A-Check'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently Active status, with flight experience on A320 aircraft",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments",
            "aircraft_status": "Aircraft AC003 status updated to Maintenance",
            "crew_certifications": "Crew certification status for A320 aircraft showing 0 crew members with certifications expiring within 30 days",
            "maintenance_records": "Aircraft maintenance records for specified period showing scheduled maintenance logs with maintenance type 'A-Check'"
        }
    ),

    Task(
        annotator="0",
        user_id="user_99",
        instruction="Manage crew operations responsible for optimizing crew scheduling and operational readiness. You need to work with: crew member CM015 (Olivia Johnson), crew member CM020 (Mohamed Lopez), role Captain, status Active. Your goals are to: ensure optimal crew placement for operational efficiency, maintain service quality standards through strategic crew management. You have access to manage: crew status updates, crew role assignments, and crew availability monitoring. The objective is to activate crew members CM015 and CM020 for operational assignments, assign CM015 to Captain role for operational leadership, and verify Captain availability for comprehensive crew management.",
        actions=[
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM015'}
            ),
            Action(
                name="GetCrewMemberInfo",
                kwargs={"crew_id": 'CM020'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM015', "new_status": 'Active'}
            ),
            Action(
                name="UpdateCrewMemberStatus",
                kwargs={"crew_member_id": 'CM020', "new_status": 'Active'}
            ),
            Action(
                name="GetCrewAvailability",
                kwargs={"role": 'Captain', "status": 'Active'}
            ),
            Action(
                name="UpdateCrew",
                kwargs={"crew_id": 'CM015', "role": 'Captain'}
            ),
        ],
        outputs={
            "crew_details_15": "Crew member CM015 (Olivia Johnson) - Captain based at ORD airport, currently Active status, with flight experience on B737 aircraft retrieved via get_crew_member_info with crew_id 'CM015' for crew management coordination",
            "crew_details_20": "Crew member CM020 (Mohamed Lopez) - Flight Attendant based at CLT airport, currently On Leave status, with flight experience on A320 aircraft retrieved via get_crew_member_info with crew_id 'CM020' for crew management coordination",
            "crew_updates": "Crew member CM015 status updated to Active, CM020 status updated to Active via update_crew_member_status actions with crew_member_id 'CM015' and 'CM020', new_status 'Active' for operational readiness",
            "crew_availability_captains": "Current availability of active Captain crew members for operational assignments retrieved via get_crew_availability with role 'Captain', status 'Active' for strategic crew placement",
            "crew_assignment": "Crew member CM015 role successfully updated to Captain for operational assignments via update_crew with crew_id 'CM015', role 'Captain' for strategic crew management"
        }
    ),

    Task(
        annotator="0",
        user_id="user_100",
        instruction="Execute senior operations management responsible for customer service operations. You need to work with: reservation NO6JO3, customer emma.smith8074@example.com, cabin class first, insurance yes, payment method credit_card_4421486, flight HAT083, date 2024-05-16, start date 2024-05-16, end date 2024-05-16, flight operations and schedule optimization. Your goals are to: deliver exceptional customer service through strategic reservation management, ensure efficient flight operations and strategic scheduling.  You have access to manage: flight status monitoring, schedule management.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetUserProfile",
                kwargs={'user_email': 'emma.smith8074@example.com'}
            ),
            Action(
                name="UpdateReservation",
                kwargs={'reservation_id': 'NO6JO3', 'cabin': 'first', 'insurance': 'yes', 'payment_method_id': 'credit_card_4421486'}
            ),
            Action(
                name="GetReservationDetails",
                kwargs={'reservation_id': 'NO6JO3'}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={'flight_number': 'HAT083', 'date': '2024-05-16'}
            ),
            Action(
                name="GetFlightSchedule",
                kwargs={'start_date': '2024-05-16', 'end_date': '2024-05-16'}
            ),
        ],
        outputs={
            "customer_profile": "Isabella Brown's customer profile including membership level, payment methods, and reservation history for NO6JO3",
            "reservation_update": "Reservation NO6JO3 successfully upgraded to first class with travel insurance, showing updated cabin class, insurance status, and payment method",
            "flight_status": "Flight HAT083 status for May 16, 2024 showing operational details, origin/destination, scheduled times, and availability",
            "daily_schedule": "Flight schedule summary for May 16, 2024 showing total flights, key operations, and coordination opportunities across the network"
        }
    ),
]