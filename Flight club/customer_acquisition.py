import requests

SHEETY_API = "https://api.sheety.co/d3889b37b31752549849bbc26d475eb1/kopiaFlightDeals/users"


def add_user_to_sheet(name, last_name, email):
    """
    Adds a user to the sheet
    """
    params = {
        "user": {
            "firstName": name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=SHEETY_API, json=params)
    print(response.text)


while True:
    print("Welcome to Dragon's Flight Club\nWe find the best flight deals and email you.")
    name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email address?\n")
    email_confirmation = input("Please confirm your email.\n")

    if email == email_confirmation:
        print("Welcome", name, last_name, "to Dragon's Flight Club.")
        add_user_to_sheet(name, last_name, email)
    else:
        print("Your email doesn't match")



