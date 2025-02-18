# PDF Image Processing and Classification API

This FastAPI-based service extracts images from a given PDF file and classifies them into predefined categories using the BLIP image captioning model.

## Features

- Extracts images from PDFs.
- Classifies images into predefined categories.
- Saves a JSON report containing image details and classification results.
- Provides an API endpoint to process PDFs.

## Installation

### Prerequisites

- Python 3.8+
- CUDA-enabled GPU (recommended but optional)

### Install Dependencies

```bash
pip install fastapi uvicorn torch transformers pillow pydantic pdf2image pymupdf
```

## Project Structure

```
.
├── main.py                 # FastAPI application
├── pdf_image_extractor.py  # Extracts images from PDFs
├── image_caption_generator.py # Classifies images using BLIP
├── requirements.txt        # List of dependencies
├── README.md               # Documentation
└── output/                 # Folder where processed images & JSON reports are saved
```

## API Usage

### Start the API Server

```bash
uvicorn main:app --reload
```

### Process a PDF

#### Endpoint

```
POST /process_pdf/
```

#### Request Body (JSON)

```json
{
  "pdf_path": "C://path_to_your_pdf/document.pdf"
}
```

#### Response (JSON)

```json
[
  {
    "image_path": "output/document_1.png",
    "image_extension": "png",
    "category": "Planning & Design"
  },
  {
    "image_path": "output/document_2.png",
    "image_extension": "png",
    "category": "Marketing & Sales"
  }
]
```

## Predefined Categories

1. **Planning & Design**
   - Master Plan, Property Plan, Architectural Plan, Interior Design Plan, Landscape Plan, Structural Plan.
2. **Financial Details**
   - Payment Plan, Mortgage Plan, ROI Analysis, Cost Breakdown, Taxation Details.
3. **Legal & Regulatory**
   - Title Deed, Zoning Rules, Permits, Lease Agreements, HOA Rules.
4. **Marketing & Sales**
   - Brochures, Virtual Tours, Comparisons, Property Videos.
5. **Amenities & Features**
   - Facilities, Smart Home Features, Security Measures.

## Saving the JSON Report

- The processed data is saved inside the output folder as `pdfname_report.json`.

## Future Improvements

- Implement CLIP for improved classification.
- Enhance confidence scoring for classifications.
- Support batch processing of multiple PDFs.

## License

MIT License

---

**Developed by:** AI Engineer | Specialized in Computer Vision 🚀

