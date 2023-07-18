import os
import boto3
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

load_dotenv()  # take environment variables from .env.

# Now you can access the variables. They are stored as strings.
db_user = os.getenv('example')

print(db_user)