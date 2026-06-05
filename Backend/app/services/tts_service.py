import requests

PIPER_URL = (
    "http://localhost:9100/tts"
)


def text_to_speech(
    text: str
):
    response = requests.post(
        PIPER_URL,
        json={
            "text": text
        }
    )

    return response.json()