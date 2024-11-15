import os
from dotenv import load_dotenv
from huggingface_hub import login


def authenticate_with_huggingface():
    """
    Authenticates with Hugging Face using a token from the .env file.
    """
    # Load the .env file
    load_dotenv()

    # Retrieve the Hugging Face token from the environment
    token = os.getenv("HUGGINGFACE_TOKEN")

    if not token:
        raise ValueError("Hugging Face token not found. Please add HUGGINGFACE_TOKEN to your .env file.")

    # Log in to Hugging Face
    login(token=token)
    print("Successfully authenticated with Hugging Face!")
