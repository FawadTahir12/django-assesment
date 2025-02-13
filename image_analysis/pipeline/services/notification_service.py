from django.core.mail import send_mail
from django.conf import settings

class NotificationService:
    def send_email(self, email, report):
        send_mail(
            subject="Your Image Analysis Report",
            message=report,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

    def send_sms(self, phone, message):
        """Send SMS notification."""
        print(f"Sending SMS to this {phone} ")
