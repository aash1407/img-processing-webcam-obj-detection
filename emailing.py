import smtplib
from email.message import EmailMessage
import imghdr
from dotenv import load_dotenv
import logging
import os

# Load environment variables from a .env file
# The dotenv_path argument specifies the exact path to the .env file
load_dotenv(dotenv_path='.env')

# Retrieve the email credentials and receiver email from the environment
# variables
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(image_path):
    """
        Sends an email with an image attachment.

        Args:
            image_path (str): The path to the image file to be attached to the email.
        """

    try:

        # Create the email message object
        email_message = EmailMessage()
        email_message["Subject"] = "New object detected!"
        email_message.set_content("Hey, we just detected a new object!!")

        # Open the image file and attach it to the email
        with open(image_path, "rb") as file:
            content = file.read()

        # Add the image as an attachment, detecting the image format
        # automatically
        email_message.add_attachment(content, maintype="image",
                                     subtype=imghdr.what(None, content))

        # Set up the SMTP server and send the email
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(EMAIL_SENDER, EMAIL_PASSWORD)
        gmail.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message.as_string())
        gmail.quit()
        logging.info("Email sent successfully!")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")


if __name__ == "__main__":
    send_email(image_path="images/19.png")
