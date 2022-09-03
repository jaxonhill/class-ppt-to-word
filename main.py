from docx import Document
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader


# def create_pages_obj_from_pdf_file(pdf_file_name):
#     """
#     Takes in the pdf file name and returns a list of the pages.
#     :param pdf_file_name: the exact name as it appears in the "Downloads" folder
#     :return: a list of PDF page objects that you can extract text from
#     """
#     full_file_path = f"C:/Users/19493/Downloads/{pdf_file_name}"
#     reader = PdfReader(full_file_path)
#     return list(reader.pages)


def create_soup_from_html_file(html_file_name):
    """
    Creates a BeautifulSoup object with the data from the HTML file you pass it

    :param html_file_name: the exact name of the HTML file as it appears in the "Downloads" folder
    :return: a BeautifulSoup object
    """
    full_file_path = f"C:/Users/19493/Downloads/{html_file_name}"
    html_content = open(full_file_path, "r", encoding="utf-8").read()
    new_soup = BeautifulSoup(html_content, "html.parser")
    return new_soup


def create_heading(chosen_document, heading_text):
    pass


# Create the soup object and Word doc object
soup = create_soup_from_html_file("chap01.html")
document = Document()
print(soup.text)


# pages_list = create_pages_obj_from_pdf_file("chap01 - Tagged.pdf")      # Retrieve the page list from chosen PDF
# # document = Document()       # Create the Word document object
#
# for page in pages_list:
#     page_text = page.extract_text()
#     new_line_list = list(page_text.split("\n"))
#     print(new_line_list[0])
#     print("__________________")

# document.add_heading("A HEADING!!")
# paragraph = document.add_paragraph("Lorem ipsum dolor sit amet.")
# document.save("C:/Users/19493/Desktop/new_word_doc.docx")

# TODO: Download the PPT file into HTML format
# TODO: Use beautifulsoup to scrape the HTML formatting
# TODO: For every h1, you would create a line break and make a heading on the page
# TODO: Everything that follows the h1, you would add below it
