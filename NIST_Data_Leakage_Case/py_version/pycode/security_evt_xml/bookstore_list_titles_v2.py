import xml.etree.ElementTree as ET

tree = ET.parse("bookstore.xml")
root = tree.getroot()

# Find and print all the "year" elements
for title_element in root.findall(".//title"):
    print(title_element.text)
