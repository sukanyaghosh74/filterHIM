# filters/ocr_filter.py
import pytesseract
from PIL import Image
import cv2
from config import TESSERACT_CMD
from filters.text_filter import contains_blocked_text

pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def scan_image_for_text(path):
    image = cv2.imread(path)
    text = pytesseract.image_to_string(image)
    return contains_blocked_text(text)
