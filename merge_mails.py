from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def merge_emails(email1, email2):
    # Create a multipart message to hold the merged content
    merged_email = MIMEMultipart("alternative")

    # Extract subject, sender, and receiver info (customize as needed)
    merged_email['Subject'] = "Merged Email: " + email1['Subject'] + " & " + email2['Subject']
    merged_email['From'] = email1['From']
    merged_email['To'] = email1['To']

    # Add email 1 content
    part1 = MIMEText(email1.get_payload(), 'html')
    merged_email.attach(part1)

    # Add a separator
    merged_email.attach(MIMEText("<hr>", 'html'))

    # Add email 2 content
    part2 = MIMEText(email2.get_payload(), 'html')
    merged_email.attach(part2)

    return merged_email

# Example usage
email1 = MIMEMultipart()
email1['Subject'] = "Email 1 Subject"
email1['From'] = "sender@example.com"
email1['To'] = "recipient@example.com"
email1.attach(MIMEText("<p>This is the content of email 1.</p>", 'html'))

email2 = MIMEMultipart()
email2['Subject'] = "Email 2 Subject"
email2['From'] = "sender@example.com"
email2['To'] = "recipient@example.com"
email2.attach(MIMEText("<p>This is the content of email 2.</p>", 'html'))

merged_email = merge_emails(email1, email2)
print(merged_email.as_string())
