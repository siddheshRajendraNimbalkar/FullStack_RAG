import requests


WHISPER_URL = (
    "http://127.0.0.1:9000/transcribe"
)


def speech_to_text(
    audio_file
):
    files = {
        "file": (
            audio_file.filename,
            audio_file.file,
            audio_file.content_type
        )
    }

    response = requests.post(
        WHISPER_URL,
        files=files
    )

    return response.json()