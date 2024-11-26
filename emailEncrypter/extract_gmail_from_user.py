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

    # login to the inbox
    mail.login(user, password)
    mail.select('inbox')

    # search for email with the encryption ID
    search_criterion = f'(HEADER Subject "{subject}")'
    status, response = mail.search(None, search_criterion)

    if status != 'OK' or not response[0]:
        return f"No emails found with subject: {subject}"

    # get the latest email ID (assuming the search results are sorted by date)
    latest_email_id = response[0].split()[-1]  # get the latest email

    # get the email with the latest ID
    status, msg_data = mail.fetch(latest_email_id, '(RFC822)')

    if status != 'OK':
        return "Failed to fetch the email."

    # process the contents of the email
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # get subject/body
    from_email = msg['from']

    # process the body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = msg.get_payload(decode=True).decode()

    # logout
    mail.logout()

    # return the contents here:
    return body
