import requests

# Set your access key
access_key = "_Qg5dTWUDOYvTVMKyFH4F6TcvgLpq09NlU4ueSeK3bA"

# Make the API request
url = "https://api.unsplash.com/photos/random?username=oscarmcgl"
headers = {
    "Accept-Version": "v1",
    "Authorization": f"Client-ID {access_key}"
}
response = requests.get(url, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    # Extract the photo URL from the response
    photo_data = response.json()
    photo_url = photo_data["urls"]["regular"]
else:
    print("Failed to retrieve a random photo from Unsplash.")
