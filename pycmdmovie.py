from PIL import Image
import os, time, cv2


ASCII_CHARS = " .:=+*#%@"
# ASCII_CHARS = "@%#*+=-:. "


def _scale_image(image, new_width=25):
    """Rescale the image to fit within the desired width while maintaining aspect ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width / 2)
    new_image = image.resize((new_width, new_height))
    return new_image


def _convert_to_grayscale(image):
    """Convert the image to grayscale."""
    return image.convert("L")


def _map_pixels_to_ascii(image, range_width=30):
    """Map each pixel to an ASCII character based on pixel intensity."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        # Ensure pixel_value is within a valid range
        pixel_index = min(int(pixel_value // range_width), len(ASCII_CHARS) - 1)
        ascii_str += ASCII_CHARS[pixel_index]
    return ascii_str


def _convert_image_to_ascii(image_path, new_width=500):
    """Convert the image to ASCII art."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Convert image to grayscale and rescale it
    image = _convert_to_grayscale(image)
    image = _scale_image(image, new_width)

    # Map pixels to ASCII characters
    ascii_str = _map_pixels_to_ascii(image)

    # Group ASCII characters into lines of text
    ascii_lines = [ascii_str[index:index+new_width] for index in range(0, len(ascii_str), new_width)]
    ascii_art = "\n".join(ascii_lines)
    return ascii_art


    time.sleep(.1)


def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def _extract_frames(video_path):
    folder = video_path.split('.')[0] + '_movie'
    if not os.path.exists(folder):
        os.makedirs(folder)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    cap.release()
    print(f'Frames extracted: {frame_count}')


def display_img(img_path):
    print(_convert_image_to_ascii(img_path))


def display_imgs(imgs_dir, *, delay=.1, clear=False, infinite=True):
    valid_extensions = ('jpg', 'jpeg', 'png')
    imgs = [img for img in os.listdir(imgs_dir) if img.split('.')[1] in valid_extensions]
    if len(imgs) == 0:
        print(f'No images found. Please consider the following image extensions: {valid_extensions}')
        return
    while True:
        for img in imgs:
            ascii_img = _convert_image_to_ascii(os.path.join(imgs_dir, img))
            print(ascii_img)
            time.sleep(delay)
            if clear:
                _clear()
        if not infinite:
            break


def display_video(video_path, *, delay=.1, clear=False, infinite=True):
    dir = video_path.split('.')[0] + '_movie'
    if not os.path.exists(dir):
        _extract_frames(video_path)
    display_imgs(dir, delay=delay, clear=clear, infinite=infinite)

