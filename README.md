Replicate Image Generation API and Fine-Tuning
----------------------------------------------
This project is a FastAPI application designed to generate images and fine-tune models using the Replicate API. It includes endpoints to create images based on prompts, fine-tune a model with custom images, and check the status of ongoing tasks.

Features
--------
Generate Image: Create images based on custom prompts with adjustable dimensions and format. \n
Fine-tune Model: Train models with custom images and configurations. \n
Task Status Check: Monitor the status of fine-tuning or image-generation tasks. \n

Project Structure
------------------
main.py: Defines the FastAPI app and the API endpoints. \n
models.py: Contains the data models used for request and response validation. \n
config.py: Manages configuration settings, including the Replicate API key. \n
