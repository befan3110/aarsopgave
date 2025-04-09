import requests

def get_data():
    # Fetch all data from the API
    url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,languages"
    headers = {'Accept': 'application/json'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        countries = response.json()
        return countries
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return []

def display_country(country):
    # Display details of a single country
    name = country.get('name', {}).get('common', 'Unknown')
    capital = country.get('capital', ['Unknown'])[0]
    flag = country.get('flags', {}).get('png', None)  # Use PNG URL for the flag
    languages = ', '.join(country.get('languages', {}).values()) or 'Unknown'

    print(f"Name: {name}")
    print(f"Capital: {capital}")
    print(f"Languages: {languages}")
    try:
        if flag:
            from IPython.display import Image, display
            display(Image(url=flag, width=250))  # Display the flag image
            print(flag)
            print("open this link to view flag")
        else:
            print("No flag available.")
    except ImportError:
        print("IPython is not available. Cannot display the flag image.")
    print("-" * 40)

def ui():
    # Function to search for countries and get user input
    countries = get_data()

    if not countries:
        print("No country data available. Exiting program.")
        return

    print("Welcome! This is a collection of different countries!")

    while True:
        print("\nCommands:")
        print("1 - Search for a country by name")
        print("2 - Search for a country by capital")
        print("3 - Exit")

        choice = input("Enter your number: ")
        if choice == "1":
            country_name = input("Enter the country name: ").lower()
            matching_countries = [
                country for country in countries
                if country_name in country.get('name', {}).get('common', '').lower()
            ]

            if matching_countries:
                print("\nMatching countries:")
                for country in matching_countries:
                    display_country(country)
            else:
                print("No countries found with that name.")

        elif choice == "2":
            capital_name = input("Enter the capital name: ").lower()
            matching_countries = [
                country for country in countries
                if capital_name in (country.get('capital', ['Unknown'])[0].lower() if country.get('capital') else '')
            ]

            if matching_countries:
                print("\nMatching countries:")
                for country in matching_countries:
                    display_country(country)
            else:
                print("No countries found with that capital.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    ui()

if __name__ == "__main__":
    main()