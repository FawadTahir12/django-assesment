from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .services.aws_service import S3Service
from .tasks import analyze_images_task

class ImageAnalysisView(APIView):
    
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        email = request.data.get('email')

        if not images:
            return Response({"error": "No images uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        # Step 1: Upload images to S3
        s3_service = S3Service()
        file_keys = s3_service.upload_images(images)

        analyze_images_task.delay(email, file_keys) #Celery task

        return Response({
            "message": "Image analysis started. Report will be sent when ready."
        }, status=status.HTTP_202_ACCEPTED)
