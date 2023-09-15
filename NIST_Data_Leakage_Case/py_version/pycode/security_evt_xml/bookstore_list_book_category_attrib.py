import xml.etree.ElementTree as ET

tree = ET.parse("bookstore_removed_ns.xml")
root = tree.getroot()

# Iterate through the book elements and print their category attributes
for book in root.findall(".//book"):  # Find all 'book' elements at any depth
    # Get book category attribute
    cate = book.attrib.get("category")
    print("book category: {}".format(cate))
