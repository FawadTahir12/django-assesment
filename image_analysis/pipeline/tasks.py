from celery import shared_task
from .models import ImageAnalysis, CustomUser
from .services.aws_service import S3Service
from .services.image_analysis import ImageAnalysisService
from .services.report_generation import ReportGenerator
from .services.notification_service import NotificationService

@shared_task
def analyze_images_task(email, file_keys):
    """Process images in a batch, generate a report, store results, and notify the user."""
    
    user = CustomUser.objects.get(email=email)
    s3_service = S3Service()
    analysis_service = ImageAnalysisService()
    report_service = ReportGenerator()
    notification_service = NotificationService()

    # Generate presigned URLs
    image_urls = s3_service.generate_presigned_urls(file_keys)

    # Perform image analysis
    analysis_results = analysis_service.analyze_images(image_urls)

    # Generate full report text
    report_text = report_service.generate_report(analysis_results)

    # Store data in the database
    image_analysis = ImageAnalysis.objects.create(
        user=user,
        uploaded_images=[{"image_url": url} for url in image_urls],  # Store S3 URLs
        analysis_report=analysis_results,  # Store JSON analysis result
    )

    # Send notifications
    if user.email:
        notification_service.send_email(user.email, report_text)

    if user.phone:
        sms_message = f"Your image analysis is complete. Report sent to {user.email}."
        notification_service.send_sms(user.phone, sms_message)

    return f"Analysis saved for user {user.email}"
