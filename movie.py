from PIL import Image
import os, time


# Define ASCII characters ordered by intensity
ASCII_CHARS = "@%#*+=-:. "


def scale_image(image, new_width=100):
    """Rescale the image to fit within the desired width while maintaining aspect ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width / 2)
    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    """Convert the image to grayscale."""
    return image.convert("L")


def map_pixels_to_ascii(image, range_width=25):
    """Map each pixel to an ASCII character based on pixel intensity."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        # Ensure pixel_value is within a valid range
        pixel_index = min(int(pixel_value // range_width), len(ASCII_CHARS) - 1)
        ascii_str += ASCII_CHARS[pixel_index]
    return ascii_str


def convert_image_to_ascii(image_path, new_width=500):
    """Convert the image to ASCII art."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Convert image to grayscale and rescale it
    image = convert_to_grayscale(image)
    image = scale_image(image, new_width)

    # Map pixels to ASCII characters
    ascii_str = map_pixels_to_ascii(image)

    # Group ASCII characters into lines of text
    ascii_lines = [ascii_str[index:index+new_width] for index in range(0, len(ascii_str), new_width)]
    ascii_art = "\n".join(ascii_lines)
    return ascii_art


def wait():
    time.sleep(.1)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    while True:
        DIR = 'rafael_movie'
        imgs = os.listdir(DIR)
        for img in imgs:
            ascii_img = convert_image_to_ascii(os.path.join(DIR, img))
            print(ascii_img)
            # print('\n' * 10)
            # wait()
            # clear()
