import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

MODEL = "meta-llama/Llama-3.1-8B-Instruct"


def generate_response(prompt, temperature=0.2, max_tokens=500):

    hf_token = os.getenv("HF_TOKEN")

    if not hf_token:
        raise RuntimeError(
            "HF_TOKEN is missing. Check your .env file."
        )

    client = InferenceClient(
        model=MODEL,
        api_key=hf_token
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are TOM, a helpful educational AI assistant. "
                    "Answer accurately, clearly, and simply for college students."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
