import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def save_to_sheet(records, sheet_url):
    # Setup Google Sheets client
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)

    # Open My Google Sheet
    sheet = client.open_by_url(sheet_url).sheet1

    # Prepare headers
    headers = [
        "Company Name",
        "Domain",
        "Industry",
        "Company Size",
        "Contact Name",
        "Job Title",
        "Work Email",
        "LinkedIn URL (Contact)",
        "LinkedIn URL (Company)",
        "Source",
        "Email Status",
        "Last Verified Date",
    ]

    sheet.clear()
    sheet.append_row(headers)

    # Extract and append data
    for rec in records:
        company_name = rec.get("orgName")
        domain = rec.get("orgWebsite")
        industry = rec.get("orgIndustry")
        company_size = rec.get("orgSize")
        contact_name = rec.get("fullName")
        job_title = rec.get("position")
        work_email = rec.get("email")
        linkedin_contact = rec.get("linkedinUrl")
        linkedin_company = rec.get("orgLinkedinUrl", [None])[0] if isinstance(rec.get("orgLinkedinUrl"), list) else rec.get("orgLinkedinUrl")
        source = "Apollo"  # static value (you can change dynamically if needed)
        email_status = rec.get("emailStatus")
        last_verified = datetime.now().strftime("%Y-%m-%d")

        row = [
            company_name,
            domain,
            industry,
            company_size,
            contact_name,
            job_title,
            work_email,
            linkedin_contact,
            linkedin_company,
            source,
            email_status,
            last_verified,
        ]

        sheet.append_row(row)

    print("✅ Data uploaded successfully!")