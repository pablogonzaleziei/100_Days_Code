#Nesting dictionary in list

def new_travel():
    new_country = input("New country: ")
    new_cities = []
    new_cities = input("Type the cities separated by comma: ")
    new_cities.split(", ")
    new_total_visits = input("How many times? ")
    new_entry = {"Country": new_country,"cities_visited": new_cities, "total_visits": new_total_visits}
    travel_log.append(new_entry)

travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
new_travel()
print(travel_log)