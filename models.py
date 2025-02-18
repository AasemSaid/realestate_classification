from pydantic import BaseModel

class ImageData(BaseModel):
    image_path: str
    image_extension: str
    description: str
