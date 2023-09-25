import xml.etree.ElementTree as ET


def count(xml_content):
    extensions = {}  


    root = ET.fromstring(xml_content)

    
    for elem in root.iter():
        text = elem.text
        if text:
            parts = text.split('.')
            if len(parts) > 1:
                extension = parts[-1]
                extensions[extension] = extensions.get(extension, 0) + 1

    return extensions


with open("domains.xml", "r") as file:
        xml_content = file.read()


domain_extensions = count(xml_content)

print("Domain Extensions and Their Counts:")
for extension, count in domain_extensions.items():
        print(extension, count)


