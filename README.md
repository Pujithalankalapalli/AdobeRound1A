# PDF Outline Extractor – Connecting the Dots Challenge

## 💡 Approach
This script uses PyMuPDF (`fitz`) to:
- Read all PDFs in `/app/input`
- Extract lines, fonts, and sizes
- Infer heading levels (H1, H2, H3) based on font size hierarchy
- Output JSON format with title and structured outline

## 📦 Build Docker
```bash
docker build --platform linux/amd64 -t mysolutionname:puji123 .
```

## 🚀 Run
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:puji123
```

Place your PDF(s) in `./input` and get the JSON output in `./output`.
