"""
Import and run models
"""
from basic_models.basic_models import Emails, Addresses, URLs, Dates

# --- Basic extraction modules --- #
Emails().extract_emails(
    "data/outputs/emails.json"
)
Addresses().extract_addresses()
URLs().parse_urls()
Dates().parse_dates()
