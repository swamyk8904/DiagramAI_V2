from PyPDF2 import PdfReader


def read_pdf(file_path):
    """
    Reads text from a PDF file and returns it as a single string.
    """

    text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:
        return f"Error reading PDF: {e}"