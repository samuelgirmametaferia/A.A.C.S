import api_client

API_URL = "https://api.example.com/v1/data"
API_KEY = "your_api_key"

headers = {
  "Authorization": f"Bearer {API_KEY}"
}

params = {
  "model": "gemma2-9b-it",
  "organization": "org_01je8naa5ffsj9t1kbh1xkg549"
}

try:
  data = retry_api_request(API_URL, headers=headers, params=params)
  print(data)
except Exception as e:
  print(f"An error occurred: {e}")