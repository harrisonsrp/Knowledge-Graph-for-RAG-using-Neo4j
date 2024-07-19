from bs4 import BeautifulSoup


def read_local_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Extract headings and paragraphs
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    paragraphs = soup.find_all('p')

    # Pair headings with paragraphs
    content = []
    current_heading = None
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if current_heading:
                content.append(current_heading)
            # Add "Section:" before the heading text
            current_heading = f"Section: {element.get_text().strip()}\n"
        elif element.name == 'p':
            if current_heading:
                current_heading += f"{element.get_text().strip()}\n"
            else:
                content.append(f"{element.get_text().strip()}\n")
    if current_heading:
        content.append(current_heading)

    return ''.join(content)


def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)


# Example file path (replace with your actual file path)
file_path = r'data\raw\Charles Maurice de Talleyrand-Périgord.html'

# Read the local HTML file
html_content = read_local_html(file_path)

# Extract text from the HTML
extracted_text = extract_text_from_html(html_content)

# Save the extracted text to a file
save_text_to_file(extracted_text, 'data/cleaned/Talleyrand.txt')

print(f"Text has been extracted and saved")
