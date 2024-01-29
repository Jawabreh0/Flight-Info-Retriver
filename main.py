import requests

class FlightInfoRetriever:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.aviationstack.com/v1/flights"

    def get_user_input(self):
        origin_city = input("Enter the origin airport code (e.g., JFK): ").strip().upper()
        destination_city = input("Enter the destination airport code (e.g., LAX): ").strip().upper()
        date = input("Enter the date (DD-MM-YYYY): ").strip()
        return origin_city, destination_city, date

    def retrieve_scheduled_flights(self, origin_city, destination_city, date):
        url = f"{self.base_url}?access_key={self.api_key}&search=1&dep_iata={origin_city}&arr_iata={destination_city}&flight_iata=&flight_icao=&date={date}"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                if data['pagination']['total'] > 0:
                    flights = data['data']
                    self.display_flight_info(flights, origin_city, destination_city, date)
                else:
                    print(f"No scheduled flights found from {origin_city} to {destination_city} on {date}.")
            else:
                print("Error retrieving flight information.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_flight_info(self, flights, origin_city, destination_city, date):
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

def main():
    api_key = "YOUR_KEY_HERE"
    flight_retriever = FlightInfoRetriever(api_key)

    origin_city, destination_city, date = flight_retriever.get_user_input()
    flight_retriever.retrieve_scheduled_flights(origin_city, destination_city, date)

if __name__ == "__main__":
    main()
