# Apollo Contacts Exporter to Google Sheet

A small Python utility that fetches contacts from the Apollo API and writes them to a Google Sheet.

Files

- `run.py` — main script that calls the Apollo API and passes results to the sheet helper.
- `sheet_utils.py` — contains `save_to_sheet(records, sheet_url)` which writes records into a Google Sheet using a service account.
- `service_account.json` — Google service account key (kept out of version control).

Requirements

- Python 3.8 or newer
- A Google Cloud service account JSON key with access to the target Google Sheet (Editor role or specific permissions).
- An Apollo API key with permission to call the mixed_people/search endpoint.

Setup

1. Create and activate a virtual environment (recommended):

   python -m venv .venv; .\.venv\Scripts\Activate

2. Install dependencies:

   python -m pip install -r requirements.txt

3. Place your Google service account JSON file in the project root and name it `service_account.json`

4. Create a `.env` file in the project root with the following variables:

   SHEET_URL=<your-google-sheet-url>
   API_KEY=<your-apollo-api-key>

   Example `.env` content:

   SHEET_URL=https://docs.google.com/spreadsheets/d/your_sheet_id
   API_KEY=abcd1234

Usage

- To run the script and upload data to the sheet:

  python run.py

Notes and caveats

- `sheet_utils.save_to_sheet` expects the Apollo response `records` to be an iterable of dicts.
- The current implementation clears the entire sheet and appends a header row before writing results.
- `service_account.json` contains sensitive keys. Do not commit it to source control.

Troubleshooting

- Authentication errors with Google Sheets: ensure the service account has at least Editor access on the target sheet (share the sheet with the service account email).
- Apollo API errors: check that `API_KEY` is correct and that the account has permission to use the endpoint.

License

- This project has no explicit license. Add a LICENSE file if you plan to publish it.
