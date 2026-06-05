from fastapi import FastAPI
from pydantic import BaseModel

import subprocess
import uuid

app = FastAPI()


class TTSRequest(BaseModel):
    text: str


@app.post("/tts")
def tts(request: TTSRequest):

    output_file = (
        f"/tmp/{uuid.uuid4()}.wav"
    )

    cmd = [
        "piper",
        "--model",
        "en_US-lessac-medium",
        "--output_file",
        output_file
    ]

    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE
    )

    process.communicate(
        input=request.text.encode()
    )

    return {
        "audio_path": output_file
    }