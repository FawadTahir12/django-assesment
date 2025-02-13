import boto3
from django.conf import settings
import uuid

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
        self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    def upload_images(self, images):  # multiple images upload on S3
    
        file_keys = []
        for image in images:
            file_key = f"uploads/{uuid.uuid4()}_{image.name}"
            self.s3_client.upload_fileobj(image, self.bucket_name, file_key)
            file_keys.append(file_key)
        return file_keys

    def generate_presigned_urls(self, file_keys, expiration=3600):
        return [
            self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': file_key},
                ExpiresIn=expiration
            )
            for file_key in file_keys
        ]
