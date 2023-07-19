import os
import boto3
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

load_dotenv()  # take environment variables from .env.

# Now you can access the variables. They are stored as strings.
# db_user = os.getenv('example')

client = boto3.client('rekognition')


photo = input("What image do you want to upload? Options: fachada.jpg, lobby.jpg ")


with open(photo, "rb") as image:
    source_bytes = image.read()

detect_objects = client.detect_labels(Image={'Bytes': source_bytes})
labels = [i["Name"] for i in detect_objects["Labels"]]

for label in labels:
    print(f"The next label is: {label}")

def refine_data(list_items):
    print(list_items)

refine_data(labels)