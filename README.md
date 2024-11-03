Replicate Image Generation API and Fine-Tuning
----------------------------------------------
This project is a FastAPI application designed to generate images and fine-tune models using the Replicate API. It includes endpoints to create images based on prompts, fine-tune a model with custom images, and check the status of ongoing tasks.

Features
--------
1) Generate Image: Create images based on custom prompts with adjustable dimensions and format.
2) Fine-tune Model: Train models with custom images and configurations. \n
3) Task Status Check: Monitor the status of fine-tuning or image-generation tasks. \n

Project Structure
------------------
1) main.py: Defines the FastAPI app and the API endpoints. \n
2) models.py: Contains the data models used for request and response validation. \n
3) config.py: Manages configuration settings, including the Replicate API key. \n
