# from PIL import Image
# import pytesseract

# image = Image.open('/home/sanjay/Downloads/Test2.png')

# text = pytesseract.image_to_string(image)

# print("Extracted Text: ")
# print(text)

import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('/home/sanjay/Downloads/Test2.png')
print(result)
