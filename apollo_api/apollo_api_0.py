import urllib.request
import json

def search_emails(keyword, filename):
    url = "https://api.apollo.io/v1/mixed_people/search"
    headers = {
        "Authorization": "asdfasdf",  # Replace YOUR_API_KEY with your actual API key
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "q_keywords": keyword
    }).encode('utf-8')
    
    request = urllib.request.Request(url, data=payload, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode('utf-8'))
            with open(filename, 'w') as file:
                for person in data.get('results', []):
                    email = person.get('email', 'N/A')
                    if email != 'N/A':
                        file.write(f"Email: {email}\n")
        print("Email information saved successfully.")
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.reason}")

# Example usage
search_emails("Shayan", "shayan_emails.txt")
