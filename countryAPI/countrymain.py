import requests

def get_data():
    #henter data
    url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,languages,currencies"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() #viser fejl i tilfælde af en dårlig status kode
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return []


def display_country(country):
    #funktionen der viser resultatet af programmet
    name = country.get('name', {}).get('common', 'Unknown')
    capital = country.get('capital', ['Unknown'])[0]
    flag = country.get('flags', {}).get('png', None)
    languages = ', '.join(country.get('languages', {}).values()) or 'Unknown'
    
    currencies = country.get('currencies', {})
    if currencies:
        currency = ', '.join([
            f"{code}: {cur.get('name', 'Unknown')} ({cur.get('symbol', 'Unknown')})"
            for code, cur in currencies.items()
        ])
    else:
        currency = 'Unknown'

    print(f"\nName: {name}")
    print(f"Capital: {capital}")
    print(f"Languages: {languages}")
    print(f"Currency: {currency}")
    try:
        if flag:
            from IPython.display import Image, display
            display(Image(url=flag, width=250))
        else:
            print("No flag available.")
    except ImportError:
        print(f"Flag URL: {flag if flag else 'No flag available.'}")
    print("-" * 40)

def ui():
    #søgefunktionen
    countries = get_data()
    if not countries:
        print("No country data available. Exiting program.")
        return

    print("Welcome! This is a collection of different countries!")

    while True:
        print("\nCommands:")
        print("1 - Search for a country by name")
        print("2 - Search for a country by capital")
        print("3 - Search for a country by currency")
        print("4 - Exit")

        choice = input("Enter your number: ").strip()

        if choice == "1":
            country_name = input("Enter the country name: ").lower()
            matching_countries = [
                country for country in countries
                if country_name in country.get('name', {}).get('common', '').lower()
            ]

        elif choice == "2":
            capital_name = input("Enter the capital name: ").lower()
            matching_countries = [
                country for country in countries
                if capital_name in (country.get('capital', [''])[0].lower() if country.get('capital') else '')
            ]

        elif choice == "3":
            currency_name = input("Enter the currency name or symbol: ").lower()
            matching_countries = [
                country for country in countries
                if 'currencies' in country and any(
                    currency_name in (currency.get('name') or '').lower() or
                    currency_name in (currency.get('symbol') or '').lower()
                    for currency in country['currencies'].values()
                )
            ]

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        if matching_countries:
            print(f"\nFound {len(matching_countries)} matching country(ies):")
            for country in matching_countries:
                display_country(country)
        else:
            print("No matching countries found.")

def main():
    ui()

if __name__ == "__main__":
    main()
