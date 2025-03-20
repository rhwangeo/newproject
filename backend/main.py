from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()

# 設定絕對路徑，確保 FastAPI 可以找到正確的目錄
BASE_DIR = Path(__file__).resolve().parent.parent  # 取得 sideproject/ 的絕對路徑
TEMPLATES_DIR = BASE_DIR / "frontend" / "templates"
STATIC_DIR = BASE_DIR / "frontend" / "static"

# 掛載靜態檔案 (讓 CSS 和 JS 可被訪問)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 設定模板路徑
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

class InputData(BaseModel):
    name: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/greet/")
def greet(data: InputData):
    return {"message": f"Hello, {data.name}!"}
