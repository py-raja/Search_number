from PyPDF2 import PdfReader
# User regular expression library
import re
# Read the PDF file
path=input("Enter the File name or Path : ")
reader = PdfReader(path)
# Find the total number of pages
number_of_pages = len(reader.pages)
# Specfy the page number
try:
    # Specfy the page number
    num=int(input(f"Enter a Page number between 1 to {number_of_pages} : "))
    if type(num)==int:
        
        page = reader.pages[num-1]
        text = page.extract_text()
        # Search for a 10-digit mobile number eg:9999999999
        match1 = re.findall(r"\d{10}", text)

        # Search for a 10-digit mobile number eg:999 9999999
        match2 = re.findall(r"\d{3}\s\d{7}", text)

        # Search for a 10-digit mobile number eg:999 999 9999
        match3 = re.findall(r"\d{3}\s\d{3}\s\d{4}", text)

        match = match1+match2+match3
        print(f"Search Results for Mobile number in Page Number {num} is")
        print(match)
except :
    num = 0
    for num in range(0, number_of_pages,1):
        page = reader.pages[num]
        text = page.extract_text()
        num+=1
        # Search for a 10-digit mobile number eg:9999999999
        match1 = re.findall(r"\d{10}", text)

        # Search for a 10-digit mobile number eg:999 9999999
        match2 = re.findall(r"\d{3}\s\d{7}", text)

        # Search for a 10-digit mobile number eg:999 999 9999
        match3 = re.findall(r"\d{3}\s\d{3}\s\d{4}", text)

        match = match1+match2+match3
        print(f"Search Results for Mobile number in Page Number {num} is")
        print(match)

input("Press enter to continue...")
