import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from pdf_image_extractor import PDFImageExtractor
from image_caption_generator import ImageCaptionGenerator

app = FastAPI()

# Pydantic model for the request body
class PDFRequest(BaseModel):
    pdf_path: str

# Pydantic model for the response body
class ImageData(BaseModel):
    image_path: str
    image_extension: str
    description: str

class PDFProcessor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.output_folder = os.path.splitext(os.path.basename(pdf_path))[0]
        self.image_extractor = PDFImageExtractor(pdf_path, self.output_folder)
        self.caption_generator = ImageCaptionGenerator()

    def process_pdf(self) -> List[ImageData]:
        """Extract images and generate descriptions."""
        image_folder = os.path.join(self.output_folder)
        image_count = self.image_extractor.extract_images()

        if image_count == 0:
            raise HTTPException(status_code=404, detail="No images found in the PDF")

        report = []
        for image_file in os.listdir(image_folder):
            if image_file.endswith(".png"):
                image_path = os.path.join(image_folder, image_file)
                description = self.caption_generator.generate_caption(image_path)
                report.append(ImageData(
                    image_path=image_path,
                    image_extension="png",
                    description=description
                ))
                
        # Save the report to a JSON file in the output folder
        json_file_path = os.path.join(self.output_folder, f"{self.output_folder}_report.json")
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump([item.dict() for item in report], json_file, ensure_ascii=False, indent=4)


        return report

@app.post("/process_pdf/")
async def process_pdf(pdf_request: PDFRequest):
    pdf_processor = PDFProcessor(pdf_request.pdf_path)
    return pdf_processor.process_pdf()
