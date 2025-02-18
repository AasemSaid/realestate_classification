from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

class ImageCaptionGenerator:
    def __init__(self):
        """Initialize the BLIP processor and model."""
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cuda")

    def generate_caption(self, image_path: str) -> str:
        """Generate caption for the given image using BLIP model."""
        raw_image = Image.open(image_path).convert('RGB')
        inputs = self.processor(raw_image, return_tensors="pt").to("cuda")
        out = self.model.generate(**inputs)
        return self.processor.decode(out[0], skip_special_tokens=True)
