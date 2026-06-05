from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from faster_whisper import WhisperModel

app = FastAPI()

model = WhisperModel(
    "large-v3",
    device="cpu",
    compute_type="int8"
)


@app.post("/transcribe")
async def transcribe(
    file: UploadFile = File(...)
):

    audio_path = f"/tmp/{file.filename}"

    with open(audio_path, "wb") as f:
        f.write(
            await file.read()
        )

    segments, info = model.transcribe(
        audio_path
    )

    text = " ".join(
        segment.text
        for segment in segments
    )

    return {
        "language": info.language,
        "text": text
    }