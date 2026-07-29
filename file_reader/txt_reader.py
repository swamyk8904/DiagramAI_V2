def read_txt(file_path):
    """
    Reads text from a TXT file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()

    except Exception as e:
        return f"Error reading TXT: {e}"