# 使用官方 Python 基本映像
FROM python:3.12

# 設定工作目錄 -在容器內建立 /backend 目錄，並將它設為當前工作目錄。之後的所有指令都會在這個目錄內執行。
WORKDIR /backend

# 複製 requirements.txt 檔案到容器，將本機專案的 requirements.txt 複製到容器的 /backend 目錄下。
COPY requirements.txt .

# 安裝依賴
#--no-cache-dir 參數可減少安裝過程中產生的暫存檔案，減少 Docker 映像大小。
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案檔案到容器,將本機的所有檔案（包含 FastAPI 程式碼）複製到容器內的 /backend 目錄。確保容器內部有完整的專案程式碼。
COPY . .

# 啟動 FastAPI 應用
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
