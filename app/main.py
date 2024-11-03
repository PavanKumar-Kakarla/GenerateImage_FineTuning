from fastapi import FastAPI, HTTPException
import replicate
from app.config import settings
from app.models import ImageGenerationRequest, ImageGenerationResponse, FineTuneRequest, FineTuneResponse

# Creating the Fast API App Instance
app = FastAPI(
    title="Replicate Image Generation API",
    description="A FastAPI app to fine-tune and generate images using the Replicate API EndPoint."
)

# Creating client to run APIs using Replicate API
client = replicate.Client(api_token=settings.REPLICATE_API_KEY)


@app.post("/generate-image", response_model=ImageGenerationResponse, description="Generate an image based on a given prompt.")
async def generate_image(request: ImageGenerationRequest):

    """
    Generates an image based on the provided prompt and other parameters.

    Args:
        request (ImageGenerationRequest): The request object containing image generation parameters.

    Returns:
        ImageGenerationResponse: A response object containing the status and generated images.

    Raises:
        HTTPException: If the request to the Replicate API fails or returns an error.
    """

    try:
        inputs={
                "prompt": request.prompt,
                "num_outputs": request.num_generations,
                "aspect_ratio": request.aspect_ratio,
                "height": request.image_height,
                "width": request.image_width,
                "output_format": request.output_format
        }

        output = client.run("bytedance/hyper-flux-8step:81946b1e09b256c543b35f37333a30d0d02ee2cd8c4f77cd915873a1ca622bad", 
        input=inputs)

        print(output)

        generate_images = [img.url for img in output]

        response = ImageGenerationResponse(
            status="Success",
            generated_images=generate_images
        )
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/fine-tune/", response_model=FineTuneResponse, description="Fine tuning the model based on given input images.")
async def fine_tune_model(request: FineTuneRequest):

    """
    Fine tuning the model based on input images and other parameters.

    Args:
        request (FineTuneRequest): The request object containing fine tuning parameters.

    Returns:
        FineTuneResponse: A response object containing the task ID and current status

    Raises:
        HTTPException: If the request to the Replicate API fails or returns an error.
    """

    try:
        # Initiate fine-tuning using the Replicate API
        training = client.trainings.create(
            destination="pavankumar-kakarla/flux-custom-model",
            version="ostris/flux-dev-lora-trainer:e440909d3512c31646ee2e0c7d6f6f4923224863a6a10c494606e79fb5844497",
            input={
                "input_images": str(request.input_images),
                "steps": request.steps,
                "optimizer": request.optimizer,
                "batch_size": request.batch_size,
                "trigger_word": request.trigger_word,
            },

        )

        response = FineTuneResponse(status=training.status, training_id=training.id)
        return response

    except Exception as e:
        print("Error details:", str(e), e.__dict__) 
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/task-status/{task_id}", response_model=FineTuneResponse, summary="Check Task Status", description="Check the status of a fine-tuning or generation task.")
async def task_status(task_id: str):

    """
    Checks the status of a fine-tuning task.

    Args:
        task_id (str): The unique identifier of the task to check.

    Returns:
        FineTuneResponse: A response object containing the task ID and current status

    Raises:
        HTTPException: If the request to the Replicate API fails or returns an error.
    """

    try:
        result = client.trainings.get(task_id)
        response = FineTuneResponse(status=result.status, training_id=result.id)
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve task status")