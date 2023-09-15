user_input = input("Please enter a character string: ")

with open("output.txt", "w") as file:

    file.write(user_input)
print(f"String '{user_input}' has been written to 'output.txt'.")

with open("output.txt", "r") as file:

        file_contents = file.read()

print("Contents of 'output.txt':")
print(file_contents)

import xml.etree.ElementTree as ET


def count(xml_content):
    extensions = {}  

    # Parse the XML content
    root = ET.fromstring(xml_content)

    
    for elem in root.iter():
        # Check if the element text ends with a domain extension
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
        print(f"{extension}: {count}")


