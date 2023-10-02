import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

tree = ET.parse("SecurityEvt_formatted.xml")
root = tree.getroot()

# Iterate through all System elements
for system_element in root.findall(".//System"):
    event_id_element = system_element.find("EventID")
    time_created_element = system_element.find("TimeCreated")

    # Check if EventID and TimeCreated elements exist
    if (
        event_id_element is not None
        and event_id_element.text == "4608"
        and time_created_element is not None
    ):
        event_id = event_id_element.text
        system_time = time_created_element.get("SystemTime")

        # Print the lists of EventID and TimeCreated values
        print("EventIDs: {} and SystemTimes: {}".format(event_id, system_time))
