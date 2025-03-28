from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://googuge.firebaseapp.com/",
    "https://googuge.web.app/",
    "http://localhost:5000",  # 允許本地測試
    "http://127.0.0.1:5000",
    "http://54.161.157.71:8000",  # 允許 EC2 直接訪問
    "https://www.googuge.org/",
    "https://googuge.org/",
    "https://newproject-aoj.pages.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允許 Firebase 前端的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 設定絕對路徑，確保 FastAPI 可以找到正確的目錄
BASE_DIR = Path(__file__).resolve().parent.parent  # 取得 sideproject/ 的絕對路徑
TEMPLATES_DIR = BASE_DIR / "public"
STATIC_DIR = BASE_DIR / "public"
# TEMPLATES_DIR = BASE_DIR / "frontend" / "templates"
# STATIC_DIR = BASE_DIR / "frontend" / "static"

# 掛載靜態檔案 (讓 CSS 和 JS 可被訪問)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 設定模板路徑
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

class InputData(BaseModel):
    name: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/greet")
async def greet(data: InputData):
    return {"message": f"Hello, {data.name}!"}
