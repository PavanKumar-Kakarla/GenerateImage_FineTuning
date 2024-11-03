from pydantic import BaseModel, HttpUrl, conint, confloat
from typing import List, Optional, Dict, Literal


# Image Generation Request Model
class ImageGenerationRequest(BaseModel):
    prompt: str
    num_generations: Optional[conint(ge=1)] = 1
    image_height: Optional[int] = 768
    image_width: Optional[int] = 768
    aspect_ratio: Optional[str] = "1:1"
    output_format: Optional[str] = "webp"
 

# Image Generation Response Model
class ImageGenerationResponse(BaseModel):
    status: str
    generated_images: Optional[List[str]] = None


# Fine Tuning Request Model
class FineTuneRequest(BaseModel):
    input_images: HttpUrl
    steps: conint(ge=1) = 1000  
    optimizer: Optional[Literal["adamw8bit", "adam", "sgd"]] = "adamw8bit"  
    batch_size: Optional[conint(ge=1)] = 1
    trigger_word: Optional[str] = "TOK"

    class Config:
        json_encoders = {HttpUrl: str}


# Fine Tuning Response Model
class FineTuneResponse(BaseModel):
    status: str
    training_id: str