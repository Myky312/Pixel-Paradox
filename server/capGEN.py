from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import random


# Generates a CAPTCHA of given length
def generateCaptchaText(n):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha = "".join(random.choices(chrs, k=n))
    return captcha

# Apply random distortions to the image
def distort_image(img, wave_amplitude=5, wave_frequency=0.05):
    # Create an array from the image
    arr = np.array(img)
    # Random distortion parameters
    phase = random.uniform(0, 2*np.pi)
    # Distort the array
    for i in range(img.size[1]):
        dx = int(wave_amplitude * np.sin(wave_frequency * i + phase))
        arr[i] = np.roll(arr[i], dx, axis=0)
    # Create an image from the distorted array
    distorted_img = Image.fromarray(arr, 'RGB')
    return distorted_img

# Create a complex CAPTCHA image
def createComplexCaptchaImage(captcha_text, img_size=(280, 80), font_size=36):
    # Create an image with white background
    img = Image.new('RGB', img_size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load a truetype or opentype font file
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate the position for each character to be drawn
    text_width, text_height = draw.textsize(captcha_text, font=font)
    start_x = (img_size[0] - text_width) // 2  # Start in the middle of the image
    start_y = (img_size[1] - text_height) // 2
    
    # Draw the text with random position and color
    for i, char in enumerate(captcha_text):
        # Apply random color to text
        text_color = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
        # Position each character with a random perturbation in the y-axis
        position_x = start_x + i * (text_width // len(captcha_text))
        position_y = start_y + random.randint(-5, 5)
        draw.text((position_x, position_y), char, font=font, fill=text_color)

    # Apply distortion to the image
    img = distort_image(img)

    # Optionally add noise and other effects here

    # Save the image to a file
    img.save("captcha.png")

    return img

# Generate a random CAPTCHA text
captcha_text = generateCaptchaText(6)

# Create and save the complex CAPTCHA image
createComplexCaptchaImage(captcha_text).show()
