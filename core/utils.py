# core/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_email(to_email, subject, message):
    """
    Send real email via SMTP (Gmail).
    """
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )
    print(f"Email sent to {to_email} with subject '{subject}'")
