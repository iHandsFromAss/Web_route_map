from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=8000)

app.mount("/css", StaticFiles(directory="templates/css"), name="css")
app.mount("/Build", StaticFiles(directory="templates/Build"), name="unity_build")
app.mount("/TemplateData", StaticFiles(directory="templates/TemplateData"), name="unity_template")
#шаблоны
templates_templates = Jinja2Templates(directory="templates")

# Рендеринг шаблона index.html из директории "templates"
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates_templates.TemplateResponse("index.html", {"request": request})

# Рендеринг шаблона index.html из директории "templates"
@app.get("/index.html", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates_templates.TemplateResponse("index.html", {"request": request})
