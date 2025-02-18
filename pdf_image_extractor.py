import fitz  # PyMuPDF
from PIL import Image
import os
import io

class PDFImageExtractor:
    def __init__(self, pdf_path: str, output_folder: str):
        self.pdf_path = pdf_path
        self.output_folder = output_folder
        self.pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    def extract_images(self):
        """Extract images from the PDF and save them in the output folder."""
        os.makedirs(self.output_folder, exist_ok=True)
        doc = fitz.open(self.pdf_path)
        image_count = 0
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))
                image_filename = os.path.join(self.output_folder, f"{self.pdf_name}_{image_count + 1}.png")
                image.save(image_filename)
                image_count += 1

        return image_count
