import xml.etree.ElementTree as ET

tree = ET.parse("securityEvt_formatted.xml")
root = tree.getroot()

# Find the first Event element
first_event = root.find(".//Event")

# Check if a Event element was found
if first_event is not None:
    # Convert the first Event element to a string with pretty formatting
    first_event_str = ET.tostring(first_event, encoding="unicode", method="xml")

    # Print the nicely formatted XML
    print(first_event_str)
else:
    print("No Event elements found in the XML.")
