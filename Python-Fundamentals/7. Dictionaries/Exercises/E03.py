countries = input().split(", ")
capitals = input().split(", ")

countries_with_capitals = {country: capital for (country, capital) in zip(countries, capitals)}

for key, value in countries_with_capitals.items():
    print(f"{key} -> {value}")
