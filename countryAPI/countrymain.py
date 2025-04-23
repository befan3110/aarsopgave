import requests

def get_data():
    # Henter data fra API
    url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,languages,currencies"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Viser fejl ved dårlig statuskode
        countries = response.json()
        return countries
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return []

def display_country(country):
    # Vis detaljer for et enkelt land baseret på søgeparametre
    name = country.get('name', {}).get('common', 'Unknown')
    capital = country.get('capital', ['Unknown'])[0]
    flag = country.get('flags', {}).get('png', None)  # Bruger PNG URL for flaget
    languages = ', '.join(country.get('languages', {}).values()) or 'Unknown'
    currency = ', '.join([f"{cur.get('name', 'Unknown')} ({cur.get('symbol', 'Unknown')})" for cur in country.get('currencies', {}).values()]) or 'Unknown'
    print(f"Currency: {currency}")

    print(f"Name: {name}")
    print(f"Capital: {capital}")
    print(f"Languages: {languages}")
    try:
        if flag:
            from IPython.display import Image, display
            display(Image(url=flag, width=250))  # Viser billede af flag
            print(flag)
            print("open this link to view flag")
        else:
            print("No flag available.")
    except ImportError:
        print("IPython is not available. Cannot display the flag image.")
    print("-" * 40)

def ui():
    # Funktion for at søge efter land med user input
    countries = get_data()

    if not countries:
        print("No country data available. Exiting program.")
        return

    print("Welcome! This is a collection of different countries!")

    while True:
        print("\nCommands:")
        print("1 - Search for a country by name")
        print("2 - Search for a country by capital")
        print("3 - search for a country by currency")
        print("4 - Exit")

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
            currency_name = input("Enter the currency name: ").lower()
            matching_countries = [
                country for country in countries
                if any(currency_name in currency.get('name', '').lower() for currency in country.get('currencies', {}).values())
            ]

            if matching_countries:
                print("\nMatching countries:")
                for country in matching_countries:
                    display_country(country)
            else:
                print("No countries found with that currency.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    ui()

if __name__ == "__main__":
    main()