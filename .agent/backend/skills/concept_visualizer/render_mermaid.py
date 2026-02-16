import argparse
import os

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({{ startOnLoad: true }});
    </script>
</head>
<body>
    <h1>{title}</h1>
    <div class="mermaid">
{mermaid_code}
    </div>
</body>
</html>
"""

def main():
    parser = argparse.ArgumentParser(description="Render Mermaid code to HTML.")
    parser.add_argument("--title", default="Diagram", help="Title of the diagram")
    parser.add_argument("--output", required=True, help="Output HTML filename")
    parser.add_argument("--input_file", help="File containing mermaid code (optional)")
    parser.add_argument("code", nargs='?', help="Mermaid code string (if not using input_file)")

    args = parser.parse_args()

    mermaid_code = ""
    if args.input_file:
        with open(args.input_file, 'r') as f:
            mermaid_code = f.read()
    elif args.code:
        mermaid_code = args.code
    else:
        print("Error: Must provide either --input_file or code argument.")
        return

    html_content = TEMPLATE.format(title=args.title, mermaid_code=mermaid_code)

    # Ensure output directory exists (if path provided)
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(args.output, 'w') as f:
        f.write(html_content)
    
    print(f"Diagram saved to {args.output}")

if __name__ == "__main__":
    main()
