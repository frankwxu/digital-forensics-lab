import xml.etree.ElementTree as ET

tree = ET.parse("bookstore.xml")
root = tree.getroot()

# Iterate through the book elements and print their titles
for book in root.findall(".//book"):  # Find all 'book' elements at any depth
    # Find the first 'title' elements at current depth
    title_element = book.find("title")
    if title_element is not None:
        print("Book Title: {}".format(title_element.text))
