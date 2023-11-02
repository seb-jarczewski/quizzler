import requests

parameters = {
    "amount": 10,  # Number of questions
    "type": "boolean",  # Type of questions
    "category": 17,  # Category number, 17 - Science & Nature
}

# Making a get request
response = requests.get(url="https://opentdb.com/api.php", params=parameters)  # Fetch the data from API with parameters
response.raise_for_status()

# Store the JSON data in a variable "data"
data = response.json()

# Store a list of questions with their properties
question_data = data["results"]

# print(question_data)
