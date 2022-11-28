import uuid

import whisper
from fastapi import FastAPI, UploadFile
from starlette.staticfiles import StaticFiles

app = FastAPI()


@app.post("/upload/")
def upload(audio: UploadFile):
    model = whisper.load_model('small')
    filename=str(uuid.uuid4())
    with open(filename, 'wb') as f:
        f.write(audio.file.read())
    return model.transcribe(filename)

app.mount("/", StaticFiles(directory="static", html=True))
