import requests
import json

def search_emails(keyword, filename):
    url = "https://api.apollo.io/v1/mixed_people/search"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  # Replace YOUR_API_KEY with your actual API key
        "Content-Type": "application/json"
    }
    payload = {
        "q_keywords": keyword,
        "enrich": ["email"]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        with open(filename, 'w') as file:
            for person in data['results']:
                email = person.get('email', 'N/A')
                file.write(f"Email: {email}\n")
        print("Email information saved successfully.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Example usage
search_emails("Shayan", "shayan_emails.txt")
