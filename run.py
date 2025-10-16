import requests
import os
from dotenv import load_dotenv
from sheet_utils import save_to_sheet

load_dotenv()

url = "https://api.apollo.io/api/v1/mixed_people/search"

# Load config from .env file
SHEET_URL = os.getenv("SHEET_URL")
API_KEY = os.getenv("API_KEY")

headers = {
    "accept": "application/json",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "authorization": f"Bearer {API_KEY}"
}

response = requests.post(url, headers=headers)

if response.ok:
    contact_list = response.json()
    
    sheet_url = "https://docs.google.com/spreadsheets/d/1hBCQiWgc2MRUXzfP6hRo8VAzgxzHGkYxNS0VLUFr0Qc"
    save_to_sheet(contact_list, sheet_url)
else:
    print(response.status_code, response.text)