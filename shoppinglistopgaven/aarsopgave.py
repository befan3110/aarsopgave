# %%
import requests

url = "https://www.dnd5eapi.co/api"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import requests

def display_spell(spell_data):
    print(f"Name: {spell_data['name']}")
    print(f"Level: {spell_data['level']}")
    print(f"Index: {spell_data['index']}")
    print(f"URL: {spell_data['url']}")
    print()

def main():
    url = "https://www.dnd5eapi.co/api/spells"
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        spells_data = response.json()
        spells = spells_data['results']

        print("Welcome to the D&D 5e Spellbook!")
        print(f"Total Spells: {spells_data['count']}\n")

        while True:
            print("Commands:")
            print("1 - List all spells")
            print("2 - Search for a spell by name")
            print("3 - Exit")

            choice = input("Enter your number: ")

            if choice == '1':
                print("\nList of Spells:")
                for spell in spells:
                    display_spell(spell)
            elif choice == '2':
                spell_name = input("Enter the spell name: ").lower()
                matching_spells = [spell for spell in spells if spell_name in spell['name'].lower()]
                print("\nMatching Spells:")
                for spell in matching_spells:
                    display_spell(spell)
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()



url = "https://www.dnd5eapi.co/api"

params= {"ability-scores": "/api/ability-scores"}

data = requests.get(url, params).json()

for key, value in data.items():
    print(key, value)

search = input("giv mig en ability score")
if search in key:
    print(f"{search} har skillet {key[search]["skills"]}")  

# %%
import requests

url = "https://www.dnd5eapi.co/api"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)




url = "https://www.dnd5eapi.co/api"

params= {"ability-scores": "/api/ability-scores"}

data = requests.get(url, params).json()

#for key, value in data.items():
#    if key == "ability-scores":
#        print(value)

def display_race(races_data):
    print(f"name: {races_data['name']}")
    print(f"Index: {races_data['index']}")
    print(f"URL: {races_data['url']}")
    print()

def main():
    url = "https://www.dnd5eapi.co/api/races"
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        races_data = response.json()
        races = races_data['results']

    print("Welcome to the D&D 5e Spellbook!")
    print(f"Total races: {races_data['count']}\n")
    while True:
        print("Commands:")
        print("1 - List all racess")
        print("2 - Search for a race by name")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nList of races:")
            for race in races:
                display_race(race)
        elif choice == "2":
            race_name = input("enter race name: ").lower()
            matching_races =[race for race in races if race_name in race["name"].lower()]
            
            print("\nMatching Races:")
            for race in matching_races:
                display_race(race)
        elif choice =="3":
            print("goodbye!")
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()                    



