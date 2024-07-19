import json
import re


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def parse_text_to_json(text):
    # Remove citations
    text = re.sub(r'\[\d+\]', '', text)

    # Split the text into sections based on 'Main-Section:'
    sections = re.split(r'\n(?=Main-Section:)', text)

    # Initialize an empty dictionary to hold the JSON structure
    json_structure = {}

    for section in sections:
        if not section.strip():
            continue

        # Match the main section header
        main_section_match = re.match(r'Main-Section: (.+)', section)
        if not main_section_match:
            print("No main section match:", section)
            continue

        main_section_name = main_section_match.group(1)
        # Extract the text following the main section header
        section_text = section[len(main_section_match.group(0)):].strip()

        # Add the main section and its content to the JSON structure
        json_structure[main_section_name] = section_text

    return json_structure


def save_json_to_file(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


input_file_path = r"data\cleaned\Napoleon.txt"
output_file_path = 'data/json/Napoleon.json'


text_data = read_text_file(input_file_path)
print("Text data read from file:", text_data[:500])


json_data = parse_text_to_json(text_data)


save_json_to_file(json_data, output_file_path)

print(f"JSON data has been saved to {output_file_path}")
print("JSON Data:", json_data)
