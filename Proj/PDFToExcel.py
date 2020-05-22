from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os


def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r',encoding='utf-8') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:

                return line.strip()
    return False


PDF_file = "C:\\MyFiles\\Proj\\main.pdf"

''' 
Part #1 : Converting PDF to images 
'''


# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file,500,poppler_path=r'C:\MyFiles\Proj\poppler-0.68.0_x86\poppler-0.68.0\bin')
print("Total pages" + str(pages))
# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pages:
    filename = "page_" + str(image_counter) + ".jpg"
    page.save(filename, 'JPEG')


    ''' 
    Part #2 - Recognizing text from the images using OCR 
    '''
    3
    # Variable to get count of total number of pages
    filelimit = image_counter - 1

    # Creating a text file to write the output

    # Iterate from 1 to total number of pages
    #for i in range(1, filelimit + 1):
    filename = 'C:\MyFiles\Proj\page_' + str(image_counter) + ".jpg"
    outfile = "C:\MyFiles\Proj\out_text.txt"
    f = open(outfile, "w", encoding='utf-8')

    # Recognize the text as string in image using pytesserct
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')

        # Finally, write the processed text to the file.
    f.write(text)

    # Close the file after writing all the text.
    f.close()

    aa = check_if_string_in_file(outfile, 'N°')
    ab = check_if_string_in_file(outfile, 'SANTIAGO,')
    ac = check_if_string_in_file(outfile, 'SENOR(ES')

    result = ab.find('SANTIAGO,')


    csvfile = open('C:\\MyFiles\\Proj\\Final.csv', 'a')
    if result!=0:
        FinalData= aa[-5:] + ';' + ab[13:result] + ';' + ac[result + 9:80] + "\n"
    else:
       FinalData = aa[-5:] + ';' + ac[11:50] + ';' + ab[10:] + "\n"
    csvfile.writelines(FinalData)
    csvfile.close()


    image_counter = image_counter + 1




