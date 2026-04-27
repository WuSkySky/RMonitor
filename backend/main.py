from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.routers import root, bash

app = FastAPI()

# 加载js
app.mount("/static", StaticFiles(directory="frontend/static"))

# 引入陆游
app.include_router(root.router) # 根页面
app.include_router(bash.router) # bash

# @app.websocket("/ws/text")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()
#     while True:
#         await ws.send_text(f"[{datetime.datetime.now()}] Hello RMonitor!")
#         await asyncio.sleep(0.001)