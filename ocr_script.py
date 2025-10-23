from paddleocr import PaddleOCR
import cv2

# Initialize PaddleOCR
ocr = PaddleOCR(use_textline_orientation=True, lang='en')

# Path to the image
img_path = 'combined.jpg'

# Perform OCR
result = ocr.ocr(img_path)

# Process and save the result as Markdown
with open('38_markdown.md', 'w') as f:
    if result and result[0]:
        for res in result[0]:
            f.write(res[1][0] + '\n')

print("OCR result saved to 38_markdown.md")
