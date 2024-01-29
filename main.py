import requests

# Your AviationStack API key
api_key = "YOUR_KEY_HERE"

# Function to retrieve scheduled flights between two cities on a specific date
def get_scheduled_flights(origin_city, destination_city, date):
    url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}&search=1&dep_iata={origin_city}&arr_iata={destination_city}&flight_iata=&flight_icao=&date={date}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            if data['pagination']['total'] > 0:
                flights = data['data']
                print(f"Scheduled flights from {origin_city} to {destination_city} on {date}:")
                for flight in flights:
                    airline_name = flight['airline']['name']
                    departure_airport = flight['departure']['airport']
                    arrival_airport = flight['arrival']['airport']
                    departure_time_utc = flight['departure']['estimated']
                    arrival_time_utc = flight['arrival']['estimated']

                    # Convert UTC time to a more readable format
                    departure_time = departure_time_utc.split('T')[1][:5]
                    arrival_time = arrival_time_utc.split('T')[1][:5]

                    print(f"Airline: {airline_name}")
                    print(f"Departure Airport: {departure_airport}")
                    print(f"Arrival Airport: {arrival_airport}")
                    print(f"Departure Time (UTC): {departure_time} UTC")
                    print(f"Arrival Time (UTC): {arrival_time} UTC")
                    print("---------")
            else:
                print(f"No scheduled flights found from {origin_city} to {destination_city} on {date}.")
        else:
            print("Error retrieving flight information.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace the following values with your specific criteria:
origin_city = "AMM"  # Replace with the IATA code of the origin city's airport.
destination_city = "IST"  # Replace with the IATA code of the destination city's airport.
date = "2024-02-01"  # Replace with the desired date in YYYY-MM-DD format.

get_scheduled_flights(origin_city, destination_city, date)
