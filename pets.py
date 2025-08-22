import requests
import os

def get_random_dog():
    response = requests.get("https://random.dog/woof.json")
    data = response.json()
    img_url = data["url"]
    print("Image URL:", img_url)

    img_response = requests.get(img_url)

    if img_response.status_code == 200:
        filename = "pet.jpg"

        with open(filename, 'wb') as f:
            f.write(img_response.content)
        print(f"Image saved as: {filename}")
    else:
        print("Failed to download image.")

