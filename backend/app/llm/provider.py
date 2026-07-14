import ollama

MODEL = "qwen2.5:3b"


def generate(messages):

    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    return response["message"]["content"]


def chat(user_message: str):

    return generate([
        {
            "role": "user",
            "content": user_message
        }
    ])