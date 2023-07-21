# import os
# import boto3
# from dotenv import load_dotenv
# from PIL import Image, ImageDraw, ImageFont

# load_dotenv()  # take environment variables from .env.

# # Now you can access the variables. They are stored as strings.
# # db_user = os.getenv('example')

# client = boto3.client('rekognition')


# photo = input("What image do you want to upload? Options: fachada.jpg, lobby.jpg ")


# with open(photo, "rb") as image:
#     source_bytes = image.read()

# detect_objects = client.detect_labels(Image={'Bytes': source_bytes})
# labels = [i["Name"] for i in detect_objects["Labels"]]

# for label in labels:
#     print(f"The next label is: {label}")

labels = ['Architecture', 'Building', 'Office Building', 'City', 'Condo', 'Housing', 'Urban', 'High Rise', 'Apartment Building', 'Tower', 'Car', 'Transportation', 'Vehicle', 'Convention Center']

def refine_data(list_items):
    print(list_items)
import openai

# Replace with your own API key
openai.api_key = ''

def refine_data(list_items):
    conversation = [{"role": "system", "content": f"utilicé el servicio de amazon rekognition para generar etiquetas de la imagen de la fachada de un hotel y obtuve esta lista: {list_items}. Necesito que mejores esta lista basándote en la descripción siguiente: El hotel está ubicado en la Alcaldía Cuajimalpa, Ciudad de México. El hotel ofrece alojamiento para familias y también tiene planes para viajes de negocios de corporaciones."}]
    print("Hola, soy ChatBunny yeyeye!")
    while(True):
        user_input = input(">>")
        conversation.append({"role":"user", "content": user_input})
        if user_input == "Close":
            break
        else:
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = conversation
            )
            conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
            print("\n" + response['choices'][0]['message']['content'] + "\n")

refine_data(labels)


