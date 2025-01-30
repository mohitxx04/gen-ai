import requests
 
def fetch_alerts(base_url, api_key, severity):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    url = f"{base_url}/api/alerts"
    response = requests.get(url, headers=headers, params={"severity": severity})
    return response.json()