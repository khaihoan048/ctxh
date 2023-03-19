import PyPDF2
import re
#496-578
# Open the PDF file in read-binary mode


def add_newlines_before_numbers(input_str):
    # Use regular expression to find all numbers in the string
    input_str = re.sub(r'\b(\d[^\d]*)\b', r'0\1', input_str)

    pattern = r'\d+'
    matches = re.findall(pattern, input_str)
    
    # Add a newline before each number and return the modified string
    for match in matches:
        if len(match) !=2:
            continue
        input_str = input_str.replace(match, '\n' + match)
        
    return input_str



with open('kttv.pdf', 'rb') as pdf_file:
    # Create a PDF reader object4
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Loop through each page in the PDF file
    for page_num in range(887,942):
        # Get the page object for the current page
        page=pdf_reader.pages[page_num]

        # Extract the text from the page
        text = page.extract_text()
        text = re.sub(r'\n(?!\d)', '', text)
        text=add_newlines_before_numbers(text)
        # Do something with the text (e.g. print it)
        print
        print(text)
