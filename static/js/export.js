document.addEventListener("DOMContentLoaded", function () {

    const pngBtn = document.getElementById("downloadPNG");
    const svgBtn = document.getElementById("downloadSVG");
    const pdfBtn = document.getElementById("downloadPDF");
    const diagramArea = document.getElementById("diagramArea");

    if (!diagramArea) return;

    // ---------------- PNG ----------------
    if (pngBtn) {
        pngBtn.addEventListener("click", function () {

            html2canvas(diagramArea, {
                scale: 2,
                backgroundColor: "#ffffff"
            }).then(canvas => {

                const link = document.createElement("a");
                link.download = "diagram.png";
                link.href = canvas.toDataURL("image/png");
                link.click();

            });

        });
    }

    // ---------------- SVG ----------------
    if (svgBtn) {
        svgBtn.addEventListener("click", function () {

            const svg = diagramArea.querySelector("svg");

            if (!svg) {
                alert("Diagram not found.");
                return;
            }

            const serializer = new XMLSerializer();
            const svgString = serializer.serializeToString(svg);

            const blob = new Blob(
                [svgString],
                { type: "image/svg+xml;charset=utf-8" }
            );

            const url = URL.createObjectURL(blob);

            const link = document.createElement("a");

            link.href = url;
            link.download = "diagram.svg";
            link.click();

            URL.revokeObjectURL(url);

        });
    }

    // ---------------- PDF ----------------
    if (pdfBtn) {
        pdfBtn.addEventListener("click", function () {

            html2canvas(diagramArea, {
                scale: 2,
                backgroundColor: "#ffffff"
            }).then(canvas => {

                const { jsPDF } = window.jspdf;

                const pdf = new jsPDF(
                    "landscape",
                    "mm",
                    "a4"
                );

                const img = canvas.toDataURL("image/png");

                const pageWidth = pdf.internal.pageSize.getWidth();
                const pageHeight = pdf.internal.pageSize.getHeight();

                pdf.addImage(
                    img,
                    "PNG",
                    5,
                    5,
                    pageWidth - 10,
                    pageHeight - 10
                );

                pdf.save("diagram.pdf");

            });

        });
    }

});