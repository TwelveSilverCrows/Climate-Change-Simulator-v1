import requests as requests
from unsplash.api import Api
from unsplash.auth import Auth
from PIL import Image
from io import BytesIO

client_id = "4Vwaw-8lwS3_QfivsLzQNvWsRhKyjiTNMXsqJ2OS7ao"
client_secret = ""
redirect_uri = ""
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)
import requests
import pygame

category = 'earth'
# Fetch image data
url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=4Vwaw-8lwS3_QfivsLzQNvWsRhKyjiTNMXsqJ2OS7ao"
data = requests.get(url).json()
print(data)
img_data = requests.get(data["urls"]["regular"]).content
dict1= 'results'
name = data["user"]
print(name)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Adjust window size as needed
pygame.display.set_caption("Unsplash Image Viewer")


# Load image from byte data
image = pygame.image.load(BytesIO(img_data))


# Resize image to fit the window (optional)
# image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the image to the screen
    screen.blit(image, (0, 0))

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
