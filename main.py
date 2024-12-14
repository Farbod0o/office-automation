from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from controller.controller import *
app = FastAPI()

templates = Jinja2Templates(directory="view/templates")
app.mount("/static", StaticFiles(directory="view/statics/"), name="static")
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit-dep")
async def submit_dep_form(
        name: str = Form(...),
        phone: str = Form(...),
        department_num: str = Form(...),
        short_description: str = Form(...),
        additional_description: str = Form(...),
        photo: UploadFile = File(...)
):

    photo_path = os.path.join(UPLOAD_FOLDER, photo.filename)
    with open(photo_path, "wb") as buffer:
        buffer.write(photo.file.read())

    status, dep = Controller.add_department(
        name, department_num, photo_path, short_description, "address", phone, additional_description
    )
    return {"status": status, "message": dep}



# uvicorn main:app --reload
