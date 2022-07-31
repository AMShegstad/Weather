import json, requests

print("Welcome to Alex Shegstad's Weather Application!\n")
location = input("Please enter your city name or zip code: \n")

base_url = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = "36e6d28280856d0437333fd3732d1b09"

url = f"{base_url}{location}&units=imperial&appid={api_key}"
print(url)
print("\n")

def get_info():
    # Obtain information to display to guest

    response = requests.get(url)
    unformatted_data = response.json()

    print(unformatted_data)

def display_results(url, location):

    response = requests.get(url)
    unformatted_data = response.json()

    print(unformatted_data)

    temp = unformatted_data["main"]["temp"]
    high = unformatted_data["main"]["temp_max"]
    low = unformatted_data["main"]["temp_min"]

    print(f"The following is the weather for {location}")
    print(f"The current temperature is {temp}")
    print(f"The high temperature is {high}")
    print(f"The low temperature is {low}")

def main():
    get_info()
    display_results(url, location)

main()

