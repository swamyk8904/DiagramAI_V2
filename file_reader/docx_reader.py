from docx import Document


def read_docx(file_path):
    """
    Reads text from a DOCX file and returns it as a single string.
    """

    try:
        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                text += paragraph.text + "\n"

        return text.strip()

    except Exception as e:
        return f"Error reading DOCX: {e}"