
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import time


def send_email(tag: str) -> None:
    """
    Email to myself
    :param tag: telegram tag which is monitoring
    :return:
    """
    # Define email details
    sender_email = "your_email@gmail.com"
    receiver_email = sender_email
    subject = f"Notifivation, tag: {tag} is available!"
    body = f"Notifivation, tag: {tag} is available!"

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    # Connect to SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()

    # Login to Gmail account
    username = sender_email
    password = "your_email_password"  # create here https://myaccount.google.com/apppasswords
    smtp_server.login(username, password)

    # Send email
    text = msg.as_string()
    smtp_server.sendmail(sender_email, receiver_email, text)
    smtp_server.quit()

    print("Email sent!")


def check_tag() -> None:
    """
    Check if tag is available every 5 minutes
    """
    tag_to_check = "telegram_tag"
    url = f"https://t.me/{tag_to_check}"
    while True:
        response = requests.get(url)
        if "If you have Telegram, you can contact" in response.text:
            send_email(tag_to_check)
            break
        time.sleep(300)


def main() -> None:
    """
    main
    """
    check_tag()


if __name__ == '__main__':
    main()
