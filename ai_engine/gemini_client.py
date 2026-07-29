import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash-lite")


def generate_diagram(extracted_text, user_prompt):
    prompt = f"""
You are an expert Mermaid diagram generator.

Return ONLY valid Mermaid syntax.
Do NOT use markdown code fences.
Do NOT explain anything.
The Mermaid code must compile without errors.

GENERAL RULES:
- Use flowchart TB (Top-to-Bottom) unless the user explicitly requests another diagram type.
- Generate diagrams optimized for A4 portrait printing.
- Keep the diagram compact.
- Avoid long horizontal layouts.
- Group related nodes under their parent node.
- If a node has many children, arrange them vertically instead of in one long row.
- Keep connectors short and readable.
- Avoid excessive whitespace.
IMPORTANT:

- A subgraph is only for grouping nodes.
- Never connect an arrow to a subgraph.
- Every device must be represented as a separate node inside its subgraph.
- Connect every Harness node to the Device node.
- The Device node should be placed in the center of the subgraph.

Example structure:

flowchart TB
subgraph G363["Device Group 363"]
    D363["Device 363"]
    H263["Harness 263"]
    H264["Harness 264"]

    H263 --> D363
    H264 --> D363
end

Diagram Types:
- ER Diagram -> erDiagram
- Flowchart -> flowchart TB
- Class Diagram -> classDiagram
- Sequence Diagram -> sequenceDiagram

If the document represents harnesses and devices:
- Place each Device in the center.
- Arrange connected Harness nodes vertically around the Device.
- If there are many Harness nodes, split them into multiple rows/columns to keep the width small.
- Prefer height over width so the diagram fits on an A4 page.

Document:
{extracted_text}

User Request:
{user_prompt}
"""

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()
        text = text.replace("```mermaid", "")
        text = text.replace("```", "")

        return text.strip()

    except Exception as e:
        return f"Error: {e}"