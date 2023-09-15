import xml.etree.ElementTree as ET

tree = ET.parse("bookstore.xml")
root = tree.getroot()

# Find the "author" element with the current name and update it
for author_element in root.findall(".//author"):
    if author_element.text == "Giada De Laurentiis":
        author_element.text = "Giada Laurentiis"

# Serialize the updated XML to a string
updated_xml_content = ET.tostring(root, encoding="utf-8")

# Print the updated XML content
print(updated_xml_content.decode("utf-8"))
