import ollama


def generate_response(user_message: str) -> str:
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response["message"]["content"]