import xml.etree.ElementTree as ET

tree = ET.parse("SecurityEvt.xml")
root = tree.getroot()

# Create an empty set to store unique tag names
tag_names = set()

# Iterate through the elements and collect unique tag names
for element in root.iter():
    tag_names.add(element.tag)

# Convert the set to a sorted list and print the tag names
tag_list = sorted(tag_names)
for tag in tag_list:
    print(tag)
