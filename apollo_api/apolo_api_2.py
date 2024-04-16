import json
import urllib.request

def fetch_tasks_data(api_key):
    url = "https://api.apollo.io/v1/tasks/search"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    }
    payload = {
        "api_key": api_key,
        "sort_by_field": "task_created_at",
        "per_page": 200,
        "open_factor_names": ["outreach_manual_email"]
    }

    try:
        req = urllib.request.Request(url, headers=headers, data=json.dumps(payload).encode('utf-8'))
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error fetching tasks data:", e)
        return None

def save_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data saved to", filename)
    except IOError as e:
        print("Error saving data to file:", e)

def main():
    api_key = "jbtkZzFFVqfs23_Xpef0Gg"  # Replace with your actual API key
    filename = "tasks_data.json"
    
    # Fetch tasks data
    tasks_data = fetch_tasks_data(api_key)
    
    if tasks_data is not None:
        # Save tasks data to a local file
        save_to_file(tasks_data, filename)

if __name__ == "__main__":
    main()
