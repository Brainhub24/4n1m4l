from docx import Document

def create_word_document(file_path, output_path):
    # Read the content from the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Create a new Word document
    document = Document()
    
    # Add the content to the document
    document.add_paragraph(content)
    
    # Save the document
    document.save(output_path)
    print(f"Word document created successfully at: {output_path}")

# Set the paths for the input text file and output Word document
input_file = 'input.txt'
output_file = 'output.docx'

# Create the Word document
create_word_document(input_file, output_file)
