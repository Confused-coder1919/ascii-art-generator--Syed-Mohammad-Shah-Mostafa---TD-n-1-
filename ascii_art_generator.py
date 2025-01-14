from PIL import Image

# ASCII characters used to create the art
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Resizes the image preserving the aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjusted for font aspect ratio
    return image.resize((new_width, new_height))

def grayify(image):
    """Converts image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Converts each pixel to a corresponding ASCII character."""
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    """Main function to handle the image to ASCII conversion."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {image_path}")
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Split ASCII string into lines of the specified width
    ascii_lines = [ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)]
    ascii_art = "\n".join(ascii_lines)
    return ascii_art

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ascii_art_generator.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    ascii_art = convert_image_to_ascii(image_path)

    if ascii_art:
        print(ascii_art)
        # Optionally save the ASCII art to a file
        with open("ascii_art_output.txt", "w") as f:
            f.write(ascii_art)
