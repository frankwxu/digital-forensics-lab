import xml.etree.ElementTree as ET

tree = ET.parse("bookstore.xml")
root = tree.getroot()


# Define a function to recursively remove all namespace prefixes
def remove_namespace_prefix(element):
    print(element.tag)
    element.tag = element.tag.split("}", 1)[-1]  # Remove namespace prefix
    for child in element:
        remove_namespace_prefix(child)


# Remove namespace prefixes from the root element and its descendants
remove_namespace_prefix(root)

# Convert the modified XML tree to a string
modified_xml = ET.tostring(root, encoding="utf-8")

# Save the updated XML to a new file
with open("bookstore_removed_ns.xml", "wb") as f:
    f.write(modified_xml)
