import xml.etree.ElementTree as ET

tree = ET.parse("bookstore.xml")
root = tree.getroot()

# Find and update all the "price" elements
for price_element in root.findall(".//price"):
    current_price = float(price_element.text)
    new_price = current_price + 1
    price_element.text = str(new_price)

# Serialize the updated XML to a string
updated_xml_content = ET.tostring(root, encoding="utf-8")

# Save the updated XML to a new file
with open("bookstore_updated_price.xml", "wb") as f:
    f.write(updated_xml_content)
