from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from controller.controller import Controller

app = FastAPI()
templates = Jinja2Templates(directory="view/templates")
app.mount("/static", StaticFiles(directory="view/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("add_organization.html", {"request": request})

@app.post("/add-organization")
async def add_organization(
    name: str = Form(...),
    slogan: str = Form(...),
    logo: str = Form(...),
    duties: str = Form(...),
    address: str = Form(...),
    telephone: str = Form(...),
    description: str = Form(""),
    head_id: int = Form(None)
):
    success, message = Controller.add_organization(name, slogan, logo, duties, address, telephone, description, head_id)
    if success:
        return {"message": "سازمان با موفقیت اضافه شد!"}
    else:
        return {"error": f"{message}"}
