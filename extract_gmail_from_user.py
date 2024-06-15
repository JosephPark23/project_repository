import imaplib
import email
import yaml

def get_body(subject):
    # Load credentials from YAML
    with open("credentials.yml") as f:
        content = f.read()

    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    user, password = my_credentials["user"], my_credentials["password"]

    # IMAP settings
    imap_url = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(imap_url)

    # Login to the mailbox
    mail.login(user, password)
    mail.select('inbox')

    # Search for emails with the specific subject
    search_criterion = f'(HEADER Subject "{subject}")'
    status, response = mail.search(None, search_criterion)

    if status != 'OK' or not response[0]:
        return f"No emails found with subject: {subject}"

    # Get the latest email ID (assuming the search results are sorted by date)
    latest_email_id = response[0].split()[-1]  # Get the latest email

    # Fetch the email with the latest ID
    status, msg_data = mail.fetch(latest_email_id, '(RFC822)')

    if status != 'OK':
        return "Failed to fetch the email."

    # Parse the email content
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Extract subject and body
    from_email = msg['from']

    # Process the email body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = msg.get_payload(decode=True).decode()

    # Logout from the mailbox
    mail.logout()

    # Return the extracted body
    return body