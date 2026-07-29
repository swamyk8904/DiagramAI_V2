import os

from flask import (
    Blueprint,
    render_template,
    request,
    current_app
)

from file_reader.excel_reader import read_excel_file
from file_reader.pdf_reader import read_pdf
from file_reader.docx_reader import read_docx
from file_reader.txt_reader import read_txt
from file_reader.csv_reader import read_csv
from file_reader.pptx_reader import read_pptx

from ai_engine.gemini_client import generate_diagram

main = Blueprint("main", __name__)


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


@main.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        uploaded_file = request.files.get("file")
        prompt = request.form.get("prompt")

        if uploaded_file and allowed_file(uploaded_file.filename):

            save_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                uploaded_file.filename
            )

            uploaded_file.save(save_path)

            extension = uploaded_file.filename.rsplit(".", 1)[1].lower()

            extracted_text = ""

            if extension == "xlsx":
                extracted_text = read_excel_file(save_path)

            elif extension == "pdf":
                extracted_text = read_pdf(save_path)

            elif extension == "docx":
                extracted_text = read_docx(save_path)

            elif extension == "txt":
                extracted_text = read_txt(save_path)

            elif extension == "csv":
                extracted_text = read_csv(save_path)

            elif extension == "pptx":
                extracted_text = read_pptx(save_path)

            else:
                extracted_text = "Unsupported file."

            try:

                mermaid_code = generate_diagram(
                    extracted_text,
                    prompt
                )

            except Exception as e:

                return render_template(
                    "index.html",
                    error=f"AI Error: {str(e)}"
                )

            return render_template(
                "index.html",
                success=True,
                filename=uploaded_file.filename,
                prompt=prompt,
                extracted_text=extracted_text,
                mermaid_code=mermaid_code
            )

        return render_template(
            "index.html",
            error="Unsupported file type."
        )

    return render_template("index.html")