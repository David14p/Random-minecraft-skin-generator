from PIL import Image
import random
import os

def generate_random_skin():
    width, height = 64, 64  # Standard Minecraft skin size
    skin = Image.new("RGB", (width, height))
    pixels = skin.load()
    
    for x in range(width):
        for y in range(height):
            pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Get the current directory of the script and save the file there
    current_dir = os.path.dirname(os.path.realpath(__file__))
    skin.save(os.path.join(current_dir, "random_skin.png"))
    print("Random Minecraft skin generated and saved as 'random_skin.png' in the current directory")

if __name__ == "__main__":
    generate_random_skin()
