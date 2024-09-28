from PIL import Image
from io import BytesIO
import time

# Set up the Gemini API key
API_KEY = os.getenv('GEMINI_API_KEY')  # Replace with your actual Gemini API key
API_URL = 'https://gemini.googleapis.com/v1/chat'

IMAGE_ID = "your_image_id"  # Replace with the actual image ID

TOTAL_SECONDS = 3600



if (TOTAL_SECONDS > 0):
    IMAGE_ID = "your_image_id"  # Replace with image of buff cat
else:
    IMAGE_ID = "your_image_id"  # Replace with image of dead cat

image = fetch_and_display_image(API_URL, IMAGE_ID, API_KEY)
image.show()

did_workout = input("Did you workout today?")

if (did_workout):
    restart_countdown

countdown



# needed for image display
def fetch_image_from_gemini(API_URL, IMAGE_ID, API_KEY=None):
    headers = {}
    
    # If an API key is needed, include it in the headers
    if API_KEY:
        headers['Authorization'] = f'Bearer {API_KEY}'

    try:
        # Make the request to the Gemini API
        response = requests.get(f"{API_URL}/images/{IMAGE_ID}", headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Open the image from the response content
            image = Image.open(BytesIO(response.content))
            return image
        else:
            print(f"Error fetching image: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
@staticmethod
def restart_countdown():
    TOTAL_SECONDS = 3600

@staticmethod
def countdown():
    while TOTAL_SECONDS:
        time.sleep(1)  # Pause for 1 second
        TOTAL_SECONDS -= 1
