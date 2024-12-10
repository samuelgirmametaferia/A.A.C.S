import requests
from time import sleep

def make_api_request(url, headers=None, params=None):
  try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
    return None

def retry_api_request(url, headers=None, params=None, max_retries=3, backoff_factor=0.3):
  retries = 0
  while retries < max_retries:
    response = make_api_request(url, headers=headers, params=params)
    if response:
      return response
    retries += 1
    print(f"API request failed, retrying in {backoff_factor * retries} seconds...")
    sleep(backoff_factor * retries)
  raise Exception(f"API request failed after {max_retries} retries.")