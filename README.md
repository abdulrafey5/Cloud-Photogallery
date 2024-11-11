# Photo Gallery Project with Django and AWS S3

This project is a Django-based photo gallery application that allows users to upload, view, and manage photos. Images are stored securely in an AWS S3 bucket to enable scalable and reliable media storage.

## Features

- User-friendly photo gallery with image upload, view, and delete functionalities
- Integrated with AWS S3 for scalable media storage
- Organized media files in the S3 bucket for easy access and management
- Publicly accessible images with secure bucket policies and permissions

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS (or any other you’ve used)
- **Storage**: AWS S3
- **Dependencies**: Django, django-storages, boto3

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all necessary packages:

```bash
pip install -r requirements.txt
```

Ensure that `django-storages` and `boto3` are included in `requirements.txt`:

```text
Django==3.2
django-storages
boto3
```

### 4. Configure AWS and Django Settings

#### AWS S3 Setup

1. **Create an S3 Bucket**: In your AWS console, create a new S3 bucket.
2. **Bucket Permissions**: Configure your bucket policy to allow public read access to objects.

   Example bucket policy:

   ```json
   {
     "Version": "2008-10-17",
     "Statement": [
       {
         "Sid": "AllowPublicRead",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::your-bucket-name/*"
       }
     ]
   }
   ```

3. **CORS Configuration**: Configure CORS for public access to the files:

   ```xml
   <CORSRule>
       <AllowedOrigin>*</AllowedOrigin>
       <AllowedMethod>GET</AllowedMethod>
       <MaxAgeSeconds>3000</MaxAgeSeconds>
       <AllowedHeader>*</AllowedHeader>
   </CORSRule>
   ```

#### Django Settings

In your Django `settings.py`, add the following configuration:

```python
# AWS Credentials
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_REGION_NAME = 'us-west-2'  # Change based on your bucket's region

# Storage settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/'
```

### 5. Apply Migrations and Start the Server

Run Django migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser to access the application.

### 6. Testing S3 Upload

To test if files upload to S3 successfully, you can use the Django shell:

```bash
python manage.py shell
```

In the shell, run the following:

```python
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

test_file = ContentFile(b'This is a test upload to S3.')
file_name = default_storage.save('test_folder/testfile.txt', test_file)
file_url = default_storage.url(file_name)
print("Uploaded file URL:", file_url)
```

If the URL points to your S3 bucket and the file is accessible, the integration is successful.

## Additional Information

- **Public Access**: Images are accessible to the public. Make sure your bucket policy reflects this or adjust as needed.
- **AWS IAM Role**: Ensure your IAM role/user has the necessary permissions for S3 actions.
