import requests
import json
import time
from datetime import datetime

def main():
    api_url = "https://zenquotes.io/api/today"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data:
            # Création d'un nom de fichier avec horodatage pour garantir l'unicité
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"/data/quotes_{timestamp}.json"
            with open(filename, "w") as file:
                json.dump(data, file)
            print(f"JSON saved successfully in {filename}.")
        else:
            print("No items in the response.")
    else:
        print("API request failed with status code:", response.status_code)

if __name__ == "__main__":
    main()

""" Use a Python base image.
Set the working directory.
Copy requirements.txt
Set python buffered to 1 (allows the Python output to be sent straight to the terminal)
Install dependencies.
Copy the app code.
Define the entry point. """
