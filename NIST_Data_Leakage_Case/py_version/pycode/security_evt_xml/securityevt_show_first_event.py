import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

tree = ET.parse("SecurityEvt_ns_removed.xml")
root = tree.getroot()

# Find the first Event element
first_event = root.find(".//Event")

# Check if a Event element was found
if first_event is not None:
    # Convert the first Event element to a string with pretty formatting
    first_event_str = ET.tostring(first_event, encoding="unicode", method="xml")

    # Parse the XML content
    dom = minidom.parseString(first_event_str)

    # Pretty print the XML content
    pretty_xml = dom.toprettyxml(indent="   ")

    # Print the nicely formatted XML
    print(pretty_xml)
else:
    print("No Event elements found in the XML.")
