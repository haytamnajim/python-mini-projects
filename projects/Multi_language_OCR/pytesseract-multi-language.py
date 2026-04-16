import pytesseract
from PIL import Image
import os

# Point to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def run_ocr(image_path, lang='eng'):
    try:
        print(f"Processing {image_path} with language '{lang}'...")
        text = pytesseract.image_to_string(Image.open(image_path), lang=lang)
        return text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Test with our generated image
    test_img = 'test_ocr.png'
    if os.path.exists(test_img):
        result = run_ocr(test_img, lang='eng')
        print("\n--- OCR Result ---")
        print(result)
        print("------------------")
    else:
        print(f"File {test_img} not found.")

    # Interactive mode (optional)
    # path = input("\nEnter image path (or 'q' to quit): ")
    # if path.lower() != 'q' and os.path.exists(path):
    #     print(run_ocr(path))
