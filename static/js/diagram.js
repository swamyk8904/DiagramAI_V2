let currentZoom = 1;

const zoomInBtn = document.getElementById("zoomInBtn");

if (zoomInBtn) {
    zoomInBtn.addEventListener("click", () => {

        currentZoom += 0.1;

        const diagram = document.querySelector("#diagramArea .mermaid");

        if (diagram) {
            diagram.style.transform = `scale(${currentZoom})`;
            diagram.style.transformOrigin = "top center";
        }

    });
}
const zoomOutBtn = document.getElementById("zoomOutBtn");

if (zoomOutBtn) {
    zoomOutBtn.addEventListener("click", () => {

        if (currentZoom > 0.2) {
            currentZoom -= 0.1;
        }

        const diagram = document.querySelector("#diagramArea .mermaid");

        if (diagram) {
            diagram.style.transform = `scale(${currentZoom})`;
            diagram.style.transformOrigin = "top center";
        }

    });
}
const resetZoomBtn = document.getElementById("resetZoomBtn");

if (resetZoomBtn) {
    resetZoomBtn.addEventListener("click", () => {

        currentZoom = 1;

        const diagram = document.querySelector("#diagramArea .mermaid");

        if (diagram) {
            diagram.style.transform = "scale(1)";
           diagram.style.transformOrigin = "top left";
        }

    });
}
const fullscreenBtn = document.getElementById("fullscreenBtn");

if (fullscreenBtn) {
    fullscreenBtn.addEventListener("click", () => {

        const diagramArea = document.getElementById("diagramArea");

        if (!document.fullscreenElement) {
            diagramArea.requestFullscreen();
        } else {
            document.exitFullscreen();
        }

    });
}
const diagramArea = document.getElementById("diagramArea");

if (diagramArea) {

    let isDragging = false;
    let startX;
    let startY;
    let scrollLeft;
    let scrollTop;

    diagramArea.addEventListener("mousedown", (e) => {
        isDragging = true;
        diagramArea.style.cursor = "grabbing";

        startX = e.pageX;
        startY = e.pageY;

        scrollLeft = diagramArea.scrollLeft;
        scrollTop = diagramArea.scrollTop;
    });

    diagramArea.addEventListener("mouseleave", () => {
        isDragging = false;
        diagramArea.style.cursor = "grab";
    });

    diagramArea.addEventListener("mouseup", () => {
        isDragging = false;
        diagramArea.style.cursor = "grab";
    });

    diagramArea.addEventListener("mousemove", (e) => {

        // ==========================
// Copy Mermaid Code
// ==========================

const copyMermaidBtn = document.getElementById("copyMermaidBtn");

if (copyMermaidBtn) {

    copyMermaidBtn.addEventListener("click", async () => {

        const mermaidCode = document.querySelectorAll(".output-box")[1]?.innerText;

        if (!mermaidCode) {
            alert("No Mermaid code found!");
            return;
        }

        try {

            await navigator.clipboard.writeText(mermaidCode);

            alert("✅ Mermaid code copied successfully!");

        } catch (err) {

            alert("❌ Failed to copy Mermaid code.");

        }

    });

}
// ==========================
// Download Mermaid (.mmd)
// ==========================

const downloadMmdBtn = document.getElementById("downloadMmdBtn");

if (downloadMmdBtn) {

    downloadMmdBtn.addEventListener("click", () => {

        const mermaidCode = document.querySelectorAll(".output-box")[1]?.innerText;

        if (!mermaidCode) {
            alert("No Mermaid code found!");
            return;
        }

        const blob = new Blob([mermaidCode], {
            type: "text/plain"
        });

        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = url;
        a.download = "diagram.mmd";

        document.body.appendChild(a);

        a.click();

        document.body.removeChild(a);

        URL.revokeObjectURL(url);

        alert("✅ .mmd file downloaded successfully!");

    });

}
        if (!isDragging) return;

        e.preventDefault();

        const x = e.pageX - startX;
        const y = e.pageY - startY;

        diagramArea.scrollLeft = scrollLeft - x;
        diagramArea.scrollTop = scrollTop - y;

    });

}