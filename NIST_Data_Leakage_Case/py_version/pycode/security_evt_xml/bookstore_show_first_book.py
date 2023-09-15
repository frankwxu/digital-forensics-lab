import xml.etree.ElementTree as ET

tree = ET.parse("bookstore.xml")
root = tree.getroot()

# Access the first child element of the root directly using indexing
first_element = root[0]

# Print the tag name and text content of the first element
print("Tag Name:", first_element.tag)
for child in first_element:
    print(f"{child.tag}: {child.text}")
