import smtplib
from email.message import EmailMessage
import imghdr

class Emailer:
    def __init__(self, origin_email: str, password_email: str) -> None:
        self.origin_email = origin_email
        self.password_email = password_email

    def set_content(self, topic: str, sender: str, contacts: list[str], email_content: str) -> None:
        self.mail = EmailMessage()
        self.mail['Subject'] = topic
        message = email_content
        self.mail['From'] = sender
        self.mail['To'] = ', '.join(contacts)
        self.mail.add_header('Content-Type', 'text/html')
        self.mail.set_payload(message.encode('utf-8'))

    def attach_images(self, images: list[str]) -> None:
        for image in images:
            with open(image, 'rb') as file:
                data = file.read()
                extension = imghdr.what(file.name)
                filename = file.name
                self.mail.add_attachment(data, maintype='image', subtype=extension, filename=filename)

    def attach_files(self, files: list[str]) -> None:
        for file in files:
            with open(file, 'rb') as f:
                data = f.read()
                filename = f.name
                self.mail.add_attachment(data, maintype='application', subtype='octet-stream', filename=filename)

    def send_email(self) -> None:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(user=self.origin_email, password=self.password_email)
            smtp.send_message(self.mail)
