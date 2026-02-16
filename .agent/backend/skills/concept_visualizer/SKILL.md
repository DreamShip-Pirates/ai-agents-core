---
name: Concept Visualizer
description: Tools to generate visual diagrams (Mermaid.js) from concepts or code.
---

# Concept Visualizer

This skill helps you generate Entity Relationship Diagrams (ERD) or Sequence Diagrams for architectural changes.

## Usage
1.  **Generate Mermaid Code**: The agent should formulate the Mermaid syntax based on the architecture.
2.  **Render to HTML**: Use the `render_mermaid.py` script to save it as an artifact.

## Script: `render_mermaid.py`
Usage: `python .agent/skills/concept_visualizer/render_mermaid.py --title "Diagram Title" --file output_name.html "meriad_code_here"`

(The script will wrap the mermaid code in an HTML template with the mermaid.js library CDN).
