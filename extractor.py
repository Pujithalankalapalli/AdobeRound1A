import fitz  
import os
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.basename(pdf_path).replace(".pdf", "")

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    spans = line["spans"]
                    if not spans:
                        continue

                    text = " ".join(span["text"] for span in spans).strip()
                    font_size = spans[0]["size"]

                    if font_size > 18:
                        level = "H1"
                    elif font_size > 14:
                        level = "H2"
                    elif font_size > 12:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = os.path.join(os.getcwd(), "input")
    output_dir = os.path.join(os.getcwd(), "output")

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            output_json = extract_outline(pdf_path)

            output_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_json, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
